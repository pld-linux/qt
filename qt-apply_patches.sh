#! /usr/bin/env bash
# Script to apply patches from qt-copy/patches/.
# See README.qt-copy for details.
#
# Lubos Lunak <l.lunak@kde.org>
# Oswald Buddenhagen <ossi@kde.org>
#

if ! test -d patches; then
    echo "No patches directory found."
    exit 1
fi

revert=false reverse=
clever=false
verbose=true silent=
for i; do
    case $i in
        -r|-R|--reverse) revert=true; reverse=--reverse;;
        -c|--clever) clever=true;;
        -s|--silent|-q|--quiet) verbose=false; silent=--silent;;
        *) echo "Unknown option '$i'." >&2; exit 1;;
    esac
done

b=../.${PWD##*/}

if $clever; then
    if ! $revert; then
        pdir=$b.patched
        odir=$b.cvs
    else
        pdir=$b.cvs
        odir=$b.patched
    fi
    $verbose && echo -n "Creating temporary copy ... "
    tdir=$b.temp
    test -d $tdir || { rm -rf $tdir.t; cp -al . $tdir.t && mv $tdir.t $tdir; } || exit
    $verbose && echo "done."
fi

plist=$b.applied
wlist=$plist.work
test -f $wlist -o ! -f $plist || cp $plist $wlist || exit
patches=`cd patches/ >/dev/null && ls [0-9]*-* $reverse`
applied=
already=
skipped=
disabled=
for file in $patches; do
    # skip files that aren't *.diff or *.patch
    test "${file%.patch}" = "$file" -a "${file%.diff}" = "$file" && continue
    pnum=${file%%-*}
    if ! $revert || ! test -f $plist; then
        # skip those having 'applied: yes' in the header
        if head -n 5 patches/$file | grep -iq '^[\t ]*applied[\t ]*:[\t ]*yes[\t ]*$'; then
            already="$already $file\n"
            continue;
        fi
        # skip disabled
        if grep -q "^[\\t ]*$pnum[\\t ]*\$" patches/DISABLED; then
            disabled="$disabled $file\n"
            continue;
        fi
    fi
    $verbose && echo -e "\nApplying: $file"
    if $clever; then
        if ! patch -b -z .touched $silent $reverse -p0 < patches/$file; then
            echo -e "\n\nPatch $file failed!"
            while :; do
                read -p "[A]bort, [c]ontinue, or [r]ollback all? " sel
                case $sel in
                    a) exit 1;;
                    c) continue 2;;
                    r)
                        $verbose && echo -ne "Deleting working directory ... "
                        rm -rf $PWD/*
                        rm -f $wlist
                        $verbose && echo -ne "done.\nSubstituting with temporary directory ... "
                        mv $tdir/* $PWD
                        rm -rf $tdir
                        $verbose && echo "done."
                        exit 2;;
                esac
            done
        fi
    else
        if ! patch $silent $reverse -p0 < patches/$file; then
            echo -e "\n\nPatch $file failed!"
            while :; do
                read -p "[A]bort or [c]ontinue? " sel
                case $sel in
                    a) exit 1;;
                    c) continue 2;;
                esac
            done
        fi
    fi
    if ! $revert; then
        echo $pnum >> $wlist
    elif test -f $wlist; then
        grep -v $pnum $wlist > $wlist.new
        mv $wlist.new $wlist
    fi
    applied="$applied $file\n"
done
touch $wlist
mv $wlist $plist

$verbose && echo -e "\n\n\nDone.\n
Applied patches:\n$applied
Previously applied patches:\n$skipped
Disabled patches:\n$disabled
Already merged patches:\n$already"

if $clever; then
    $verbose && echo -n "Creating backup ... "
    test -f $odir/.cleanme && rm -rf $odir
    for j in $(find -name \*.touched); do
        rj=${j%.touched}
        if ! test -f "$odir/$rj"; then
            mkdir -p "$odir/${rj%/*}" || exit
            ln "$tdir/$rj" "$odir/$rj" || exit
        fi
        rm "$j"
    done
    $verbose && echo -ne "done.\nDeleting temporary directory ... "
    mv $tdir $tdir.t && rm -rf $tdir.t
    if test -d $pdir; then
        $verbose && echo -ne "done.\nRestoring previous backup ... "
        for j in $(find $pdir -type f); do
            rj=${j#"$pdir/"}
            cmp -s "$j" "$rj" && { mv "$j" "$rj" || exit; }
        done
        $verbose && echo -ne "done.\nCleaning previous backup ... "
        find $pdir -type d | sort -r | xargs -r rmdir 2> /dev/null
        touch $pdir/.cleanme 2> /dev/null
    fi
    $verbose && echo "done."
fi

exit 0
