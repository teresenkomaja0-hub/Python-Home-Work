import requests
import pytest

# --- Конфигурационные параметры ---
# ВАЖНО: вставьте сюда ваш реальный базовый URL API
BASE_URL = "https://your.api.domain"  # <-- замените на реальный API URL

# ВАЖНО: вставьте сюда ваш токен авторизации
TOKEN = "YOUR_ACCESS_TOKEN"  # <-- вставьте сюда токен

headers = {
    "Authorization": f"Bearer {TOKEN}",  # или другой способ авторизации, если нужен
    "Content-Type": "application/json"
}

# --- Фикстура для автоматического создания и удаления тестового проекта ---
@pytest.fixture
def create_project():
    # Данные для создания проекта (обязательные поля)
    data = {
        "name": "Test Project Fixture",
        "description": "Created for testing"
        # добавьте сюда обязательные поля из документации
    }
    # Создаем проект
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=headers, json=data)
    assert response.status_code == 201, f"Не удалось создать проект: {response.text}"
    project = response.json()

    yield project

    # После теста — удаляем проект (если API позволяет)
    # ОПЦИЯ: добавить удаление, если API поддерживает
    # requests.delete(f"{BASE_URL}/api-v2/projects/{project['id']}", headers=headers)
    # или оставить как есть, если удаление не обязательно

# ---------------------- ТЕСТЫ ----------------------

# ================== POST /api-v2/projects ==================

def test_create_project_positive():
    data = {
        "name": "New Test Project",
        "description": "Positive test case"
        # Обязательные параметры — добавьте в соответствии с документацией
    }
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=headers, json=data)
    assert response.status_code == 201, f"Позитив: Ожидается 201, получено {response.status_code}"
    resp_json = response.json()
    assert resp_json["name"] == data["name"]
    # Можно дополнительно проверить другие обязательные параметры

def test_create_project_negative():
    # Отсутствуем обязательное поле 'name'
    data = {
        "description": "Missing name field"
    }
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=headers, json=data)
    assert response.status_code == 400 or response.status_code == 422, f"Ожидалось 400 или 422, получено {response.status_code}"

# ================== GET /api-v2/projects/{id} ==================

def test_get_project_positive(create_project):
    project_id = create_project["id"]
    response = requests.get(f"{BASE_URL}/api-v2/projects/{project_id}", headers=headers)
    assert response.status_code == 200, f"Получение проекта: ожидается 200, получено {response.status_code}"
    data = response.json()
    assert data["id"] == project_id
    assert data["name"] == create_project["name"]

def test_get_project_negative():
    invalid_id = "non-existing-id"
    response = requests.get(f"{BASE_URL}/api-v2/projects/{invalid_id}", headers=headers)
    assert response.status_code == 404 or response.status_code == 400, f"Для несуществующего проекта ожидается 404, получено {response.status_code}"

# ================== PUT /api-v2/projects/{id} ==================

def test_update_project_positive(create_project):
    project_id = create_project["id"]
    update_data = {
        "name": "Updated Name",
        "description": "Updated description"
    }
    response = requests.put(f"{BASE_URL}/api-v2/projects/{project_id}", headers=headers, json=update_data)
    assert response.status_code == 200, f"Обновление: ожидается 200, получено {response.status_code}"
    resp_json = response.json()
    assert resp_json["name"] == update_data["name"]
    assert resp_json["description"] == update_data["description"]

def test_update_project_negative():
    invalid_id = "non-existing-id"
    update_data = {
        "name": "Should Fail"
    }
    response = requests.put(f"{BASE_URL}/api-v2/projects/{invalid_id}", headers=headers, json=update_data)
    assert response.status_code == 404 or response.status_code == 400, f"Для несуществующего проекта ожидается 404, получено {response.status_code}"
