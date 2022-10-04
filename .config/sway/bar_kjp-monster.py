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
				format_down='{interface}:',
				interface='enp0s31f6',
				detached_down=True
				)

status.register('mem',format='Mem:{percent_used_mem}%')

status.register('temp',format="{temp:3.0f}°C",)

status.register('cpu_usage',format='{usage_cpu11:3}%',dynamic_color=True)
status.register('cpu_usage',format='{usage_cpu10:3}%',dynamic_color=True)
status.register('cpu_usage',format='{usage_cpu9:3}%',dynamic_color=True)
status.register('cpu_usage',format='{usage_cpu8:3}%',dynamic_color=True)
status.register('cpu_usage',format='{usage_cpu7:3}%',dynamic_color=True)
status.register('cpu_usage',format='{usage_cpu6:3}%',dynamic_color=True)
status.register('cpu_usage',format='{usage_cpu5:3}%',dynamic_color=True)
status.register('cpu_usage',format='{usage_cpu4:3}%',dynamic_color=True)
status.register('cpu_usage',format='{usage_cpu3:3}%',dynamic_color=True)
status.register('cpu_usage',format='{usage_cpu2:3}%',dynamic_color=True)
status.register('cpu_usage',format='{usage_cpu1:3}%',dynamic_color=True)
status.register('cpu_usage',format='{usage_cpu0:3}%',dynamic_color=True)

status.register('mpd',format='{status} : {artist} - {album} - {title}')

status.run()
