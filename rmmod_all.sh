# Remove all modules used in examples

echo "Remove device files"
rm /dev/fpga_led
rm /dev/fpga_dot
rm /dev/fpga_buzzer
rm /dev/fpga_dip_switch
rm /dev/fpga_fnd
rm /dev/fpga_push_switch
rm /dev/fpga_step_motor
rm /dev/fpga_text_lcd

echo "Remove kernel modules"
rmmod ./09.fpga_example/fpga_led/fpga_led_driver.ko
rmmod ./09.fpga_example/fpga_dot/fpga_dot_driver.ko
rmmod ./09.fpga_example/fpga_buzzer/fpga_buzzer_driver.ko
rmmod ./09.fpga_example/fpga_dip_switch/fpga_dip_switch_driver.ko
rmmod ./09.fpga_example/fpga_fnd/fpga_fnd_driver.ko
rmmod ./09.fpga_example/fpga_push_switch/fpga_push_switch_driver.ko
rmmod ./09.fpga_example/fpga_step_motor/fpga_step_motor_driver.ko
rmmod ./09.fpga_example/fpga_text_lcd/fpga_text_lcd_driver.ko

echo "Remove interface driver"
rmmod ./09.fpga_interface_driver/fpga_interface_driver.ko
