# Test Results: Petstore API - Pet Section

## **Summary**

- **Total Tests:** 12  
- **Passed:** 8 ✅  
- **XFailed (Known Bugs):** 4 🟠  
- **Failed:** 0 ❌

---

## **Detailed Results**

| **Test Case ID**   | **Test Description**                                           | **Status** | **Bug Reference** |
|------------------- |-------------------------------------------------------------- |----------- |----------------- |
| **TC-PET-01**     | Add a New Pet with Valid Data                                 | ✅ Pass    |                  |
| **TC-PET-02**     | Add a Pet with Missing Fields                                | 🟠 XFail   | BUG-101          |
| **TC-PET-03**     | Update an Existing Pet with Valid Data                       | ✅ Pass    |                  |
| **TC-PET-04**     | Update a Pet with Invalid ID                                | 🟠 XFail   | BUG-102          |
| **TC-PET-05**     | Find Pets with Status 'Available'                           | ✅ Pass    |                  |
| **TC-PET-06**     | Find Pets with Invalid Status                              | 🟠 XFail   | BUG-103          |
| **TC-PET-09**     | Find a Pet with Valid ID                                   | ✅ Pass    |                  |
| **TC-PET-10**     | Find a Pet with Invalid ID                                | ✅ Pass    |                  |
| **TC-PET-13**     | Delete a Pet with Valid ID                                | ✅ Pass    |                  |
| **TC-PET-14**     | Delete a Pet with Invalid ID                             | ✅ Pass    |                  |
| **TC-PET-15**     | Upload a Valid Image                                     | ✅ Pass    |                  |
| **TC-PET-16**     | Upload an Invalid File                                   | 🟠 XFail   | BUG-104          |

---

## **Summary by Status**
- ✅ **Passed:** 8 (67%)  
- 🟠 **XFailed (Known Bugs):** 4 (33%)  
- ❌ **Failed:** 0 (0%)  

Total Test Coverage: **100%** (Including XFails)  

---

## **Next Steps**
1. Monitor the status of all **4 known bugs** until they are resolved.
2. Re-run the tests once the bugs are fixed and update this document accordingly.

---
