# Bugs List: Petstore API - Pet Section

This document tracks the known bugs encountered during API testing of the **Petstore API - Pet Section**. Each bug is logged with a unique ID, description, affected test cases, and current status.

---

## **Bug Summary**

| **Bug ID** | **Description**                                                 | **Affected Endpoints**                              | **Test Case ID**               | **Status** |
|------------|-----------------------------------------------------------------|--------------------------------------------------|-------------------------------|-----------|
| 🐞 BUG-101   | POST /pet: Missing `name` returns 200 instead of 400             | `POST /pet`                                      | TC-PET-02                      | Open      |
| 🐞 BUG-102   | PUT /pet: Invalid ID returns 200 instead of 404                  | `PUT /pet`                                       | TC-PET-04                      | Open      |
| 🐞 BUG-103   | GET /pet/findByStatus: Invalid status returns 200 instead of 400 | `GET /pet/findByStatus`                         | TC-PET-06                      | Open      |
| BUG-104   | POST /pet/{petId}/uploadImage: Invalid file returns 200 instead of 400 | `POST /pet/{petId}/uploadImage`                 | TC-PET-16                      | Open      |

---

## **Detailed Bug Descriptions**

### 🐞 **BUG-101: POST /pet - Missing `name` Returns 200 Instead of 400**
- **Description:** When attempting to add a pet without the required `name` field, the API returns `200 OK` instead of the expected `400 Bad Request`.
- **Endpoint:** `POST /pet`
- **Affected Test Case:** `TC-PET-02: Add a Pet with Missing Fields`
- **Steps to Reproduce:**
  1. Prepare a JSON payload without the `name` field.
  2. Send a `POST` request to `/pet`.
  3. Observe that the response status is `200 OK` instead of `400 Bad Request`.
- **Expected Behavior:** The API should return `400 Bad Request` with an appropriate error message.
- **Status:** Open

---

### 🐞 **BUG-102: PUT /pet - Invalid ID Returns 200 Instead of 404**
- **Description:** When attempting to update a pet using an invalid ID (e.g., `-9999`), the API returns `200 OK` instead of the expected `404 Not Found`.
- **Endpoint:** `PUT /pet`
- **Affected Test Case:** `TC-PET-04: Update a Pet with Invalid ID`
- **Steps to Reproduce:**
  1. Prepare a JSON payload with an invalid ID (e.g., `-9999`).
  2. Send a `PUT` request to `/pet`.
  3. Observe that the response status is `200 OK` instead of `404 Not Found`.
- **Expected Behavior:** The API should return `404 Not Found` with an appropriate error message.
- **Status:** Open

---

### 🐞 **BUG-103: GET /pet/findByStatus - Invalid Status Returns 200 Instead of 400**
- **Description:** When searching for pets using an invalid status value (e.g., `"invalid_status"`), the API returns `200 OK` instead of the expected `400 Bad Request`.
- **Endpoint:** `GET /pet/findByStatus`
- **Affected Test Case:** `TC-PET-06: Find Pets with Invalid Status`
- **Steps to Reproduce:**
  1. Specify an invalid status value (e.g., `"invalid_status"`).
  2. Send a `GET` request to `/pet/findByStatus`.
  3. Observe that the response status is `200 OK` instead of `400 Bad Request`.
- **Expected Behavior:** The API should return `400 Bad Request` with an appropriate error message.
- **Status:** Open

### 🐞 **BUG-104: POST /pet/{petId}/uploadImage - Invalid File Returns 200 Instead of 400**
- **Description:** When attempting to upload an invalid file (e.g., `invalid_image.txt`) instead of an image, the API returns `200 OK` instead of the expected `400 Bad Request`.
- **Endpoint:** `POST /pet/{petId}/uploadImage`
- **Affected Test Case:** `TC-PET-16: Upload an Invalid File`
- **Steps to Reproduce:**
  1. Prepare an invalid file (e.g., `invalid_image.txt`).
  2. Send a `POST` request to `/pet/1/uploadImage` with the file attached.
  3. Observe that the response status is `200 OK` instead of `400 Bad Request`.
- **Expected Behavior:** The API should return `400 Bad Request` with an appropriate error message.
- **Status:** Open

---

## **Bug Status Legend**
- **Open:** Bug is identified and needs to be fixed.
- **In Progress:** Bug is currently being fixed.
- **Fixed:** Bug has been resolved.
- **Closed:** Bug has been verified as fixed.

---

## **Next Steps**
- Continue tracking these bugs until they are resolved.
- Once a bug is fixed, update the **Status** and verify the corresponding test case.

---
