import pytest
import allure
from common_steps_api import post_request, put_request, get_request, delete_request, load_payload
import os

file_path_valid = os.path.join(os.path.dirname(__file__), "payloads", "valid_image.jpg")
file_path_invalid = os.path.join(os.path.dirname(__file__), "payloads", "invalid_image.txt")

@allure.feature("Petstore API - Pet Section")
class TestPetstoreAPI:

    @allure.story("Add a New Pet")
    def test_add_pet_valid(self):
        """TC-PET-01: Add a New Pet with Valid Data"""
        payload = load_payload("add_pet.json")
        response = post_request("/pet", data=payload)
        assert response.status_code == 200
        assert response.json()["name"] == payload["name"]

    @pytest.mark.xfail(reason="BUG-101: API returns 200 instead of 400 for missing 'name'")
    @allure.story("Add a New Pet with Missing Fields")
    def test_add_pet_missing_fields(self):
        """TC-PET-02: Add a Pet with Missing Fields (Expected to Fail)"""
        payload = load_payload("add_pet.json")
        payload.pop("name")
        response = post_request("/pet", data=payload)
        assert response.status_code == 400  # Expected 400, currently returns 200


    @allure.story("Update an Existing Pet")
    def test_update_pet_valid(self):
        """TC-PET-03: Update an Existing Pet with Valid Data"""
        payload = load_payload("update_pet.json")
        response = put_request("/pet", data=payload)
        assert response.status_code == 200
        assert response.json()["name"] == payload["name"]

    @pytest.mark.xfail(reason="BUG-102: API returns 200 instead of 404 for invalid ID")
    @allure.story("Update an Existing Pet with Invalid ID")
    def test_update_pet_invalid_id(self):
        """TC-PET-04: Update a Pet with Invalid ID (Expected to Fail)"""
        payload = load_payload("update_pet.json")
        payload["id"] = -9999
        response = put_request("/pet", data=payload)
        assert response.status_code == 404  # Expected 404, currently returns 200

    @allure.story("Find Pets by Status")
    def test_find_pet_by_status(self):
        """TC-PET-05: Find Pets with Status Available"""
        response = get_request("/pet/findByStatus", params={"status": "available"})
        assert response.status_code == 200
        assert len(response.json()) > 0

    @pytest.mark.xfail(reason="BUG-103: API returns 200 instead of 400 for invalid status")
    @allure.story("Find Pets by Invalid Status")
    def test_find_pet_by_invalid_status(self):
        """TC-PET-06: Find Pets with Invalid Status (Expected to Fail)"""
        response = get_request("/pet/findByStatus", params={"status": "invalid_status"})
        assert response.status_code == 400  # Expected 400, currently returns 200


    @allure.story("Find Pet by ID")
    def test_find_pet_by_valid_id(self):
        """TC-PET-09: Find a Pet with Valid ID"""
        response = get_request("/pet/1")
        assert response.status_code == 200

    def test_find_pet_by_invalid_id(self):
        """TC-PET-10: Find a Pet with Invalid ID"""
        response = get_request("/pet/9999999")
        assert response.status_code == 404

    @allure.story("Delete a Pet")
    def test_delete_pet_valid(self):
        """TC-PET-13: Delete a Pet with Valid ID"""
        response = delete_request("/pet/1")
        assert response.status_code == 200

    def test_delete_pet_invalid(self):
        """TC-PET-14: Delete a Pet with Invalid ID"""
        response = delete_request("/pet/9999999")
        assert response.status_code == 404

    @allure.story("Upload a Valid Image")
    def test_upload_valid_image(self):
        """TC-PET-15: Upload a Valid Image"""
        file_path = os.path.join(os.path.dirname(__file__), "payloads", "valid_image.jpg")
        assert os.path.exists(file_path), "Missing test file: valid_image.jpg"
        with open(file_path, "rb") as image:
            response = post_request("/pet/1/uploadImage", files={"file": image})
            assert response.status_code == 200

    @allure.story("Upload an Invalid File")
    @pytest.mark.xfail(reason="BUG-104: API returns 200 instead of 400 for invalid file upload")
    def test_upload_invalid_image(self):
        """TC-PET-16: Upload an Invalid File (Expected to Fail)"""
        file_path = os.path.join(os.path.dirname(__file__), "payloads", "invalid_image.txt")
        assert os.path.exists(file_path), "Missing test file: invalid_image.txt"
        with open(file_path, "rb") as image:
            response = post_request("/pet/1/uploadImage", files={"file": image})
            assert response.status_code == 400, f"BUG-104: Expected 400, got {response.status_code}"

