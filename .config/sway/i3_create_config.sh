#!/usr/bin/bash

hostname=$(hostname)
i3_config_file="$HOME/.i3/config"
i3_config_dir="$HOME/.i3/config.d"

if [[ -f $i3_config_file ]];
then
	rm $i3_config_file
fi

touch $i3_config_file

echo "#### DO NOT EDIT THIS FILE, IT IS GENERATED." >> $i3_config_file
echo "#### EDIT THE FILES HERE: ~/.i3/config.d/**/*" >> "$i3_config_file"
echo "" >> $i3_config_file
echo "" >> $i3_config_file

cat $i3_config_dir/base.conf >> $i3_config_file
cat $i3_config_dir/keybindings.conf >> $i3_config_file
# cat $i3_config_dir/statusbar.conf >> $i3_config_file
cat $i3_config_dir/$hostname.conf >> $i3_config_file
cat $i3_config_dir/stuff.conf >> $i3_config_file
