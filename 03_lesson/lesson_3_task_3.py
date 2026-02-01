from address import Address
from mailing import Mailing

# Создаем адреса
to_address = Address("00100", "Хельсинки", "Миконкату", "10", "20")
from_address = Address("871991", "Санкт-Петербург", "15 линия ВО", "72", "9")

# Создаем почтовое отправление+
mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=12000.00,
    track="RB123456789RU"
)

# Выводим информацию об отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.postal_code}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.postal_code}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")