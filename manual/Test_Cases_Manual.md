# Test Cases: Pet Section
### Petstore API Manual Testing

---

## 1. POST /pet - Add a New Pet

### TC-PET-01: Add a New Pet with Valid Data (Positive)
- **Test Case ID:** TC-PET-01
- **Description:** Verify that a pet can be added using valid JSON payload
- **Preconditions:** API is accessible, valid payload available
- **Test Steps:**
  1. Prepare a valid JSON payload with pet details (ID, name, category, status, tags, photoUrls)
  2. Send a `POST` request to `/pet`
- **Expected Result:** Response status is `200 OK` and body contains pet's ID and name
- **Actual Result:** _To be filled during execution_
- **Status:** Pass/Fail

---

### TC-PET-02: Add a Pet with Missing Fields (Negative)
- **Test Case ID:** TC-PET-02
- **Description:** Verify that adding a pet with missing fields results in a validation error
- **Preconditions:** API is accessible, invalid payload available
- **Test Steps:**
  1. Prepare a JSON payload missing the pet's name
  2. Send a `POST` request to `/pet`
- **Expected Result:** Response status is `400 Bad Request` with validation error message
- **Actual Result:** _To be filled during execution_
- **Status:** Pass/Fail

---

## 2. PUT /pet - Update an Existing Pet

### TC-PET-03: Update an Existing Pet with Valid Data (Positive)
- **Test Case ID:** TC-PET-03
- **Description:** Verify that a pet can be updated using valid JSON payload
- **Preconditions:** API is accessible, existing pet ID available
- **Test Steps:**
  1. Prepare a valid JSON payload with updated pet details
  2. Send a `PUT` request to `/pet`
- **Expected Result:** Response status is `200 OK` and body contains updated pet details
- **Actual Result:** _To be filled during execution_
- **Status:** Pass/Fail

---

### TC-PET-04: Update a Pet with an Invalid ID (Negative)
- **Test Case ID:** TC-PET-04
- **Description:** Verify that updating a pet with an invalid ID results in an error
- **Preconditions:** API is accessible, invalid pet ID provided
- **Test Steps:**
  1. Prepare a JSON payload with an invalid pet ID
  2. Send a `PUT` request to `/pet`
- **Expected Result:** Response status is `404 Not Found` with pet not found message
- **Actual Result:** _To be filled during execution_
- **Status:** Pass/Fail

---

## 3. GET /pet/findByStatus - Find Pets by Status

### TC-PET-05: Find Pets with Status "Available" (Positive)
- **Test Case ID:** TC-PET-05
- **Description:** Verify that pets with status "available" can be retrieved
- **Preconditions:** API is accessible, pets with status "available" exist
- **Test Steps:**
  1. Specify the status as "available"
  2. Send a `GET` request to `/pet/findByStatus`
- **Expected Result:** Response status is `200 OK` and response body contains a list of pets
- **Actual Result:** _To be filled during execution_
- **Status:** Pass/Fail

---

### TC-PET-06: Find Pets with Invalid Status (Negative)
- **Test Case ID:** TC-PET-06
- **Description:** Verify that using an invalid status results in an error
- **Preconditions:** API is accessible
- **Test Steps:**
  1. Specify an invalid status value
  2. Send a `GET` request to `/pet/findByStatus`
- **Expected Result:** Response status is `400 Bad Request` with an invalid status message
- **Actual Result:** _To be filled during execution_
- **Status:** Pass/Fail

---

## 4. GET /pet/findByTags - Find Pets by Tags

### TC-PET-07: Find Pets by Valid Tag (Positive)
- **Test Case ID:** TC-PET-07
- **Description:** Verify that pets with a valid tag can be retrieved
- **Preconditions:** API is accessible, pets with the specified tag exist
- **Test Steps:**
  1. Specify a valid tag in the query parameters
  2. Send a `GET` request to `/pet/findByTags`
- **Expected Result:** Response status is `200 OK` and response body contains pets with the specified tag
- **Actual Result:** _To be filled during execution_
- **Status:** Pass/Fail

---

### TC-PET-08: Find Pets by Invalid Tag (Negative)
- **Test Case ID:** TC-PET-08
- **Description:** Verify that using a non-existent tag results in an error
- **Preconditions:** API is accessible
- **Test Steps:**
  1. Specify a non-existent tag
  2. Send a `GET` request to `/pet/findByTags`
- **Expected Result:** Response status is `404 Not Found` with no pets found message
- **Actual Result:** _To be filled during execution_
- **Status:** Pass/Fail

---

## 5. GET /pet/{petId} - Find Pet by ID

### TC-PET-09: Find a Pet with Valid ID (Positive)
- **Test Case ID:** TC-PET-09
- **Description:** Verify that a pet can be retrieved using a valid ID
- **Preconditions:** API is accessible, valid pet ID exists
- **Test Steps:**
  1. Use a valid pet ID
  2. Send a `GET` request to `/pet/{petId}`
- **Expected Result:** Response status is `200 OK` and response body contains the pet's details
- **Actual Result:** _To be filled during execution_
- **Status:** Pass/Fail

---

### TC-PET-10: Find a Pet with Invalid ID (Negative)
- **Test Case ID:** TC-PET-10
- **Description:** Verify that using an invalid pet ID results in an error
- **Preconditions:** API is accessible
- **Test Steps:**
  1. Use an invalid pet ID
  2. Send a `GET` request to `/pet/{petId}`
- **Expected Result:** Response status is `404 Not Found` with pet not found message
- **Actual Result:** _To be filled during execution_
- **Status:** Pass/Fail

---

## 6. POST /pet/{petId} - Update a Pet Using Form Data

### TC-PET-11: Update a Pet's Name Using Form Data (Positive)
- **Test Case ID:** TC-PET-11
- **Description:** Verify that a pet's name can be updated using form data
- **Preconditions:** API is accessible, valid pet ID exists
- **Test Steps:**
  1. Use a valid pet ID
  2. Send a `POST` request to `/pet/{petId}` with form data containing a new name
- **Expected Result:** Response status is `200 OK` and response confirms the update
- **Actual Result:** _To be filled during execution_
- **Status:** Pass/Fail

---

### TC-PET-12: Update a Pet with Invalid Form Data (Negative)
- **Test Case ID:** TC-PET-12
- **Description:** Verify that using invalid form data results in an error
- **Preconditions:** API is accessible, valid pet ID exists
- **Test Steps:**
  1. Use a valid pet ID
  2. Send a `POST` request to `/pet/{petId}` with invalid form data
- **Expected Result:** Response status is `400 Bad Request` with validation error
- **Actual Result:** _To be filled during execution_
- **Status:** Pass/Fail

---

## 7. DELETE /pet/{petId} - Delete a Pet

### TC-PET-13: Delete a Pet with Valid ID (Positive)
- **Test Case ID:** TC-PET-13
- **Description:** Verify that a pet can be deleted using a valid ID
- **Preconditions:** API is accessible, valid pet ID exists
- **Test Steps:**
  1. Use a valid pet ID
  2. Send a `DELETE` request to `/pet/{petId}`
- **Expected Result:** Response status is `200 OK` and response confirms deletion
- **Actual Result:** _To be filled during execution_
- **Status:** Pass/Fail

---

### TC-PET-14: Delete a Pet with Invalid ID (Negative)
- **Test Case ID:** TC-PET-14
- **Description:** Verify that using an invalid pet ID results in an error
- **Preconditions:** API is accessible
- **Test Steps:**
  1. Use an invalid pet ID
  2. Send a `DELETE` request to `/pet/{petId}`
- **Expected Result:** Response status is `404 Not Found` with pet not found message
- **Actual Result:** _To be filled during execution_
- **Status:** Pass/Fail

---

## 8. POST /pet/{petId}/uploadImage - Upload an Image

### TC-PET-15: Upload a Valid Image (Positive)
- **Test Case ID:** TC-PET-15
- **Description:** Verify that an image can be uploaded using a valid pet ID
- **Preconditions:** API is accessible, valid pet ID exists, valid image file available
- **Test Steps:**
  1. Use a valid pet ID
  2. Attach a valid image file
  3. Send a `POST` request to `/pet/{petId}/uploadImage`
- **Expected Result:** Response status is `200 OK` and response confirms image upload
- **Actual Result:** _To be filled during execution_
- **Status:** Pass/Fail

---

### TC-PET-16: Upload an Invalid File (Negative)
- **Test Case ID:** TC-PET-16
- **Description:** Verify that uploading an invalid file results in an error
- **Preconditions:** API is accessible, valid pet ID exists, invalid file available
- **Test Steps:**
  1. Use a valid pet ID
  2. Attach an invalid file (wrong format)
  3. Send a `POST` request to `/pet/{petId}/uploadImage`
- **Expected Result:** Response status is `400 Bad Request` with invalid file format message
- **Actual Result:** _To be filled during execution_
- **Status:** Pass/Fail

---
