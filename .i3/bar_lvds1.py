import subprocess
from i3pystatus import Status

status = Status(standalone=True)

status.register("clock",format="%a %-d %b %H:%M KW%V",)

status.register('pulseaudio',
				format='♪:{volume:3}%',
				multi_colors=True,
				#muted='M',
				color_muted = '#00FF00',
				color_unmuted = '#FF0000'
				)

status.register('network',
				format_up='{quality:5.1f}%',
				format_down='',
				interface='wlan0',
				dynamic_color = True
				)

status.register('network',
				format_up='{interface}: {v4} @ {essid}',
				format_down='{interface}:',
				interface='wlan0',
				dynamic_color = False
				)

status.register('network',
				format_down='{interface}:',
				detached_down=True
				)

status.register('battery',
				format='{status} {consumption:.2f}W {percentage:.2f}% {remaining:%E%hh:%Mm}',
				alert=True,
				alert_percentage=5,
				status={"DIS": "↓","CHR": "↑","FULL": "=",}
				)

status.register('mem',format='Mem:{percent_used_mem}%')

status.register('temp',format="{temp:3.0f}°C",)

status.register('cpu_usage',format='{usage_cpu3:3}%',dynamic_color=True)
status.register('cpu_usage',format='{usage_cpu2:3}%',dynamic_color=True)
status.register('cpu_usage',format='{usage_cpu1:3}%',dynamic_color=True)
status.register('cpu_usage',format='{usage_cpu0:3}%',dynamic_color=True)

status.register('mpd',format='{status} : {artist} - {album} - {title}')

status.run()
