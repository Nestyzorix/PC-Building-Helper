from django.core.management import BaseCommand
from backend_api.models import Processor, CoolingSystem, Motherboard, RAM, Videocard, HDD, SSD, PowerUnit


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Create processors')

        processors_info = [
            ['Intel', 'Intel Core i3-10100F', 3600, 'LGA1200', 4, 6290],
            ['Intel', 'Intel Core i3-10300F', 3700, 'LGA1200', 4, 16580],
            ['Intel', 'Intel Core i3-12100F', 3300, 'LGA1700', 4, 10630],
            ['Intel', 'Intel Core i5-10400F', 2900, 'LGA1200', 6, 13180],
            ['Intel', 'Intel Core i5-11400F', 2600, 'LGA1200', 6, 14880],
            ['Intel', 'Intel Core i5-12400F', 2500, 'LGA1700', 6, 17850],
            ['Intel', 'Intel Core i7-10700F', 2900, 'LGA1200', 8, 25080],
            ['Intel', 'Intel Core i7-11700F', 2500, 'LGA1200', 8, 29330],
            ['Intel', 'Intel Core i7-12700F', 3600, 'LGA1700', 12, 36980],
            ['Intel', 'Intel Core i9-10900F', 2800, 'LGA1200', 10, 42080],
            ['Intel', 'Intel Core i9-11900F', 2500, 'LGA1200', 8, 44630],

            ['AMD', 'AMD Ryzen 5 3600', 3600, 'AM4', 6, 12330],
            ['AMD', 'AMD Ryzen 5 5600X', 3700, 'AM4', 6, 21680],
            ['AMD', 'AMD Ryzen 7 3800X', 3900, 'AM4', 8, 27630],
            ['AMD', 'AMD Ryzen 7 5800X', 3800, 'AM4', 8, 29330],
            ['AMD', 'AMD Ryzen 9 5900X', 3700, 'AM4', 12, 38250],
            ['AMD', 'AMD Ryzen 9 5950X', 3400, 'AM4', 16, 63750]
        ]

        for item in processors_info:
            processor, created = Processor.objects.get_or_create(name=item[1], firm=item[0], frequency=item[2],
                                                                 socket=item[3], core_number=item[4], price=item[5])
        self.stdout.write(self.style.SUCCESS('Processors created'))

        cooling_system_info = [
            ['Intel Box', 'Intel', 1200, 430],
            ['DeepCool Mini', 'DeepCool', 1600, 1280],
            ['Deepcool GAMMAXX 300 R', 'Deepcool', 2000, 1870],
            ['DEEPCOOL AK620 ZERO DARK', 'Deepcool', 1500, 7140],
            ['AMD Original TM', 'AMD', 1200, 1280]
        ]

        for item in cooling_system_info:
            colsys, created = CoolingSystem.objects.get_or_create(name=item[0], firm=item[1], rotational_speed=item[2],
                                                                  price=item[3])

        self.stdout.write(self.style.SUCCESS('Cooling_systems created'))

        motherboard_info = [
            ['Gigabyte A520M', 'Gigabyte', 'AMD A520', 'AM4', 6550],
            ['Gigabyte B450M', 'Gigabyte', 'AMD B450', 'AM4', 6630],
            ['Gigabyte H410M', 'Gigabyte', 'Intel H410M', '1200', 6380],
            ['Gigabyte B460M', 'Gigabyte', 'Intel B460', '1200', 8590],
            ['ASUS PRIME B550M', 'ASUS', 'AMD B550', 'AM4', 11730],
            ['ASUS PRIME B460M', 'ASUS', 'Intel B460', '1200', 9520],
            ['ASUS B660M-K PRIME', 'ASUS', 'Intel B660', '1700', 15130],
            ['MSI MAG B550M BAZOOKA', 'MSI', 'AMD B550M', 'AM4', 11760],
            ['MSI PRO Z790-P DDR4 GAMING', 'MSI', 'Intel Z690 D4', '1700', 25500],
        ]

        for item in motherboard_info:
            motherboards, created = Motherboard.objects.get_or_create(name=item[0], firm=item[1], chipset=item[2],
                                                                      socket=item[3], price=item[4])
        self.stdout.write(self.style.SUCCESS('Motherboards created'))

        ram_info = [
            ['8Гб Kingston HyperX Fury', 'Kingston', 'DDR-4', 3000, 8, 3740],
            ['8Гб Kingston HyperX Fury 3600', 'Kingston', 'DDR-4', 3600, 8, 5870],
            ['16Гб Kingston HyperX Fury', 'Kingston', 'DDR-4', 3000, 16, 6720],
            ['32Гб Kingston HyperX Fury', 'Kingston', 'DDR-4', 3600, 32, 16580],
            ['16Гб DDR5 VULCAN', 'MICRONE', 'DDR-5', 5600, 16, 7570]
        ]

        for item in ram_info:
            rams, created = RAM.objects.get_or_create(name=item[0], firm=item[1], memory_type=item[2],
                                                      clock_frequency=item[3], memory_size=item[4],
                                                      price=item[5])

        self.stdout.write(self.style.SUCCESS('RAMs created'))

        videocard_info = [
            ['GEFORCE GTX 1650 4Гб', 'Nvidia', 4, 18280],
            ['GEFORCE GT 1030 2Гб', 'Nvidia', 2, 8930],
            ['GEFORCE RTX 3050 8 Гб', 'Nvidia', 8, 27630],
            ['PALIT GЕFORCE RTX 3060 12Гб', 'PALIT', 12, 37830],
            ['GIGABYTE GЕFORCE RTX 3070 8Гб GAMING', 'GIGABYTE', 8, 65030],
            ['MSI GEFORCE RTX VENTUS 3080 10 Гб', 'MSI', 10, 109650],
            ['GIGABYTE GEFORCE RTX 4070 12Гб', 'GIGABYTE', 12, 81350],
            ['PALIT RTX 4080 GAMING PRO 16 Гб', 'PALIT', 16, 126400],
            ['ASUS ROG GEFORCE RTX 4090 24 STRIX', 'ASUS', 24, 224800]
        ]

        for item in videocard_info:
            videocards, created = Videocard.objects.get_or_create(name=item[0], firm=item[1], memory_size=item[2],
                                                                  price=item[3])

        self.stdout.write(self.style.SUCCESS('Videocards created'))

        hdd_info = [
            ['1 Тб Western Digital', 'Western Digital', 1000, 5700],
            ['1 Тб Seagate', 'Seagate', 1000, 5020],
            ['1 Тб Toshiba', 'Toshiba', 1000, 5020],
            ['2 Тб Western Digital', 'Western Digital', 2000, 7230],
            ['2 Тб Seagate', 'Seagate', 2000, 7140],
            ['2 Тб Toshiba', 'Toshiba', 2000, 7230]
        ]

        for item in hdd_info:
            hdds, created = HDD.objects.get_or_create(name=item[0], firm=item[1], memory_size=item[2],
                                                      price=item[3])

        self.stdout.write(self.style.SUCCESS('HDDs created'))

        ssd_info = [
            ['120 Гб Kingston', 'Kingston', 120, 2380],
            ['250 Гб Samsung 970 EVO Plus', 'Samsung', 250, 5020],
            ['960 Гб Kingston', 'Kingston', 960, 8250],
            ['1000 Гб Gigabyte Aorus M.2', 'Gigabyte', 1000, 19130]
        ]

        for item in ssd_info:
            ssds, created = SSD.objects.get_or_create(name=item[0], firm=item[1], memory_size=item[2],
                                                      price=item[3])

        self.stdout.write(self.style.SUCCESS('SSDs created'))

        power_unit_info = [
            ['500W Zalman', 500, 3570],
            ['500W AeroCool KCAS', 500, 4080],
            ['600W AeroCool KCAS', 600, 4310],
            ['600W Zalman', 600, 4420],
            ['700W CoolerMaster', 700, 6290],
            ['750W Gigabyte GP-P750GM', 750, 43070],
            ['850W Thermaltake PRO RGB', 850, 12330],
            ['1000W Zalman', 1000, 13770]
        ]

        for item in power_unit_info:
            power_units, created = PowerUnit.objects.get_or_create(name=item[0], power=item[1], price=item[2],)

        self.stdout.write(self.style.SUCCESS('Power_units created'))
