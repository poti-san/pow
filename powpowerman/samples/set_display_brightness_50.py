# 画面の明るさを50%に設定する。

from powpowerman import PowerScheme
from powpowerman.knownguid import PowerKnownSettingGuid

display_subgroup = PowerScheme.active_scheme().subgroup_display
display_brightness = display_subgroup.settings(PowerKnownSettingGuid.video_devicepowerpolicy_brightness())
display_brightness.ac_value_index = 50
# display_brightness.ac_value_index = 100

display_brightness.apply_changes()

pass
