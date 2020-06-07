# Install all modules used in examples

echo "Install interface driver"
insmod ./09.fpga_interface_driver/fpga_interface_driver.ko

echo "install kernel modules"
insmod ./09.fpga_example/fpga_led/fpga_led_driver.ko
insmod ./09.fpga_example/fpga_dot/fpga_dot_driver.ko
insmod ./09.fpga_example/fpga_buzzer/fpga_buzzer_driver.ko
insmod ./09.fpga_example/fpga_dip_switch/fpga_dip_switch_driver.ko
insmod ./09.fpga_example/fpga_fnd/fpga_fnd_driver.ko
insmod ./09.fpga_example/fpga_push_switch/fpga_push_switch_driver.ko
insmod ./09.fpga_example/fpga_step_motor/fpga_step_motor_driver.ko
insmod ./09.fpga_example/fpga_text_lcd/fpga_text_lcd_driver.ko

echo "create device files"
mknod /dev/fpga_led c 260 0
mknod /dev/fpga_dot c 262 0
mknod /dev/fpga_buzzer c 264 0
mknod /dev/fpga_dip_switch c 266 0
mknod /dev/fpga_fnd c 261 0
mknod /dev/fpga_push_switch c 265 0
mknod /dev/fpga_step_motor c 267 0
mknod /dev/fpga_text_lcd c 263 0
