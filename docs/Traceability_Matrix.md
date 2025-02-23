# Traceability Matrix: Petstore API - Pet Section

---

## **Overview**
The traceability matrix maps API endpoints to test scenarios, manual test cases, and automated test cases to ensure complete coverage.

---

## **Matrix Table**

| **API Endpoint**                      | **Test Scenario**                                      | **Manual Test Case ID** | **Automation Test ID** |
|------------------------------------- |----------------------------------------------------- |------------------------ |----------------------- |
| **POST /pet**                        | Add a New Pet with Valid Data (Positive)             | TC-PET-01               | AT-PET-01              |
|                                     | Add a Pet with Missing Fields (Negative)             | TC-PET-02               | AT-PET-02              |
| **PUT /pet**                         | Update an Existing Pet with Valid Data (Positive)    | TC-PET-03               | AT-PET-03              |
|                                     | Update a Pet with an Invalid ID (Negative)           | TC-PET-04               | AT-PET-04              |
| **GET /pet/findByStatus**            | Find Pets with Status "Available" (Positive)         | TC-PET-05               | AT-PET-05              |
|                                     | Find Pets with Invalid Status (Negative)             | TC-PET-06               | AT-PET-06              |
| **GET /pet/findByTags**              | Find Pets by Valid Tag (Positive)                    | TC-PET-07               | AT-PET-07              |
|                                     | Find Pets by Invalid Tag (Negative)                  | TC-PET-08               | AT-PET-08              |
| **GET /pet/{petId}**                 | Find a Pet with Valid ID (Positive)                  | TC-PET-09               | AT-PET-09              |
|                                     | Find a Pet with Invalid ID (Negative)                | TC-PET-10               | AT-PET-10              |
| **POST /pet/{petId}**                | Update a Pet's Name Using Form Data (Positive)       | TC-PET-11               | AT-PET-11              |
|                                     | Update a Pet with Invalid Form Data (Negative)       | TC-PET-12               | AT-PET-12              |
| **DELETE /pet/{petId}**              | Delete a Pet with Valid ID (Positive)                 | TC-PET-13               | AT-PET-13              |
|                                     | Delete a Pet with Invalid ID (Negative)               | TC-PET-14               | AT-PET-14              |
| **POST /pet/{petId}/uploadImage**    | Upload a Valid Image (Positive)                       | TC-PET-15               | AT-PET-15              |
|                                     | Upload an Invalid File (Negative)                     | TC-PET-16               | AT-PET-16              |

---

## **Legend**
- **Manual Test Case IDs:** Prefixed with `TC-` (e.g., `TC-PET-01`)
- **Automation Test IDs:** Prefixed with `AT-` (e.g., `AT-PET-01`)
- Each endpoint is linked to both positive and negative test scenarios.

---

## **Traceability Notes**
- All **Manual Test Cases** are documented in `Test_Cases_Manual.md`.
- All **Automation Test Cases** will be implemented in `test_petstore.py`.
- The test coverage ensures both **Functional** and **Negative** paths are verified.

---

### **Summary**
- This traceability matrix ensures comprehensive coverage of the **Pet** section of the Petstore API.
- Each API endpoint is mapped to corresponding manual and automated test cases for traceability and validation.

---
