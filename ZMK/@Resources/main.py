import asyncio
from winsdk.windows.devices.bluetooth import BluetoothLEDevice
from winsdk.windows.storage.streams import DataReader
from winsdk.windows.devices.bluetooth.genericattributeprofile import GattCommunicationStatus
import time
import os


flag_file_path = "C:\\Users\\Luerl\\Documents\\Rainmeter\\Skins\\ZMK\\@Resources\\flagfile.txt"

BATTERY_SERVICE_UUID = "0000180f-0000-1000-8000-00805f9b34fb"
BATTERY_LEVEL_CHARACTERISTIC_UUID = "00002a19-0000-1000-8000-00805f9b34fb"

MAIN_DEVICE_HANDLE = 17
PERIPHERAL_DEVICE_HANDLE = 22

async def main():
    device_address = 0xf086b05fbc24
    device = await BluetoothLEDevice.from_bluetooth_address_async(device_address)
    if device:
        with open("C:\\Users\\Luerl\\Documents\\Rainmeter\\Skins\\ZMK\\@Resources\\device_name.txt", "w") as file:
            file.write(str(device.name))
        while True:
            if not os.path.exists(flag_file_path):
                print("Файл-флаг не найден. Завершение работы.")
                break
            services_result = await device.get_gatt_services_async()
            services = services_result.services
            for service in services:
                if str(service.uuid) == BATTERY_SERVICE_UUID:
                    characteristics_result = await service.get_characteristics_async()
                    characteristics = characteristics_result.characteristics

                    for characteristic in characteristics:
                        if str(characteristic.uuid) == BATTERY_LEVEL_CHARACTERISTIC_UUID:
                            read_result = await characteristic.read_value_async()
                            if read_result.status == GattCommunicationStatus.SUCCESS:
                                reader = DataReader.from_buffer(read_result.value)
                                battery_level = reader.read_byte()

                                device_type = "Неизвестное устройство"
                                if characteristic.attribute_handle == MAIN_DEVICE_HANDLE:
                                    device_type = "Главное устройство"
                                    with open("C:\\Users\\Luerl\\Documents\\Rainmeter\\Skins\\ZMK\\@Resources\\battery_level_main.txt", "w") as file:
                                        file.write(str(battery_level))
                                elif characteristic.attribute_handle == PERIPHERAL_DEVICE_HANDLE:
                                    device_type = "Зависимое устройство"
                                    with open("C:\\Users\\Luerl\\Documents\\Rainmeter\\Skins\\ZMK\\@Resources\\battery_level_peripheral.txt", "w") as file:
                                        file.write(str(battery_level))

                                print(f"{device_type} Battery Level: {battery_level}%")
            time.sleep(5)

asyncio.run(main())
