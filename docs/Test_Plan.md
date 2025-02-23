# Test Plan: Petstore API - Pet Section

---

## 1. Introduction
This document outlines the test plan for validating the **Pet** section of the Petstore Swagger API. The objective is to ensure that the API endpoints function correctly, handle valid and invalid requests appropriately, and meet the expected requirements.

---

## 2. Scope
- Test the following endpoints:
  - `POST /pet/{petId}/uploadImage` - Upload an image
  - `POST /pet` - Add a new pet
  - `PUT /pet` - Update an existing pet
  - `GET /pet/findByStatus` - Find pets by status
  - `GET /pet/findByTags` - Find pets by tags
  - `GET /pet/{petId}` - Find a pet by ID
  - `POST /pet/{petId}` - Update a pet using form data
  - `DELETE /pet/{petId}` - Delete a pet

- Cover both **Positive** and **Negative** scenarios.
- Use **Manual Testing** with Postman and **Automated Testing** with Pytest and Allure.

---

## 3. Testing Types
- **Functional Testing:** Verify that API endpoints return expected responses for valid inputs.
- **Negative Testing:** Ensure that API returns appropriate errors for invalid inputs.
- **Boundary Testing:** Test API behavior with edge-case values.
- **Performance Testing (Optional):** Measure API response times and load handling.

---

## 4. Tools & Technologies
- **Manual Testing:** [Postman](https://www.postman.com/)
- **Automation Testing:** Pytest + Allure
- **Version Control:** GitHub
- **IDE:** Visual Studio Code (VS Code)

---

## 5. Environment Setup
- **Base URL:** https://petstore.swagger.io/v2
- **Test Data:** Stored as JSON payloads in `/automation/payloads`
- **Response Validation:** Verify response status codes, headers, and response body structure.

---

## 6. Test Data
- JSON payloads for valid and invalid pet data:
  - `add_pet.json` - Payload for adding a new pet
  - `update_pet.json` - Payload for updating pet details
  - `create_user.json` - Payload for creating a user (if needed)

- Image files for testing the `/uploadImage` endpoint:
  - `valid_image.jpg`
  - `invalid_image.txt`

---

## 7. Test Execution
### **Manual Testing:**
- Execute test cases using **Postman**.
- Validate API requests, responses, and response times.
- Log any defects found during testing.

### **Automation Testing:**
- Execute automated tests using **Pytest**.
- Generate test reports using **Allure**.
- Validate test results using Allure's HTML reports.

---

## 8. Deliverables
- Test Plan (`Test_Plan.md`)
- Test Scenarios (`Test_Scenarios.md`)
- Manual Test Cases (`Test_Cases_Manual.md`)
- Automated Test Scripts (`test_petstore.py`)
- Allure Test Reports (`/automation/reports/allure-report`)
- Traceability Matrix (`Traceability_Matrix.xlsx`)

---

## 9. Test Schedule
| Phase              | Start Date | End Date |
|--------------------|------------|----------|
| Test Planning      | 2024-02-21 | 2024-02-23 |
| Test Design        | 2024-02-23 | 2024-02-26 |
| Manual Execution   | 2024-02-26 | 2024-02-28 |
| Automation         | 2024-02-28 | 2024-03-02 |
| Reporting          | 2024-03-02 | 2024-03-03 |

---

## 10. Risks & Mitigation
- **API Downtime:** Use mock responses if the API is unavailable.
- **Data Conflicts:** Use unique data for each test run to prevent conflicts.
- **Automation Failures:** Ensure payloads are correctly formatted and match the API specifications.

---

## 11. Approval
- **Prepared By:** Yurii Oleksovskyi
- **Reviewed By:** N/A
- **Approved By:** N/A

---