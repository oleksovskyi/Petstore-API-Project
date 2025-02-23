# Test Scenarios: Pet Section
### Petstore API Testing

---

## 1. POST /pet - Add a New Pet

```gherkin
Scenario 1.1: Add a New Pet with Valid Data (Positive)
Given I have a valid JSON payload with pet details (ID, name, category, status, tags, photoUrls)
When I send a POST request to /pet
Then The response status should be 200 OK
And The response body should contain the pet's ID and name
gherkin

Scenario 1.2: Add a Pet with Missing Fields (Negative)
Given I have a JSON payload missing the pet's name
When I send a POST request to /pet
Then The response status should be 400 Bad Request
And The response should indicate a validation error
```

## 2. PUT /pet - Update an Existing Pet
```gherkin
Scenario 2.1: Update an Existing Pet with Valid Data (Positive)
Given I have a valid JSON payload with updated pet details
When I send a PUT request to /pet
Then The response status should be 200 OK
And The response body should contain the updated pet details

Scenario 2.2: Update a Pet with an Invalid ID (Negative)
Given I have a JSON payload with an invalid pet ID
When I send a PUT request to /pet
Then The response status should be 404 Not Found
And The response should indicate that the pet was not found
```

## 3. GET /pet/findByStatus - Find Pets by Status
```gherkin
Scenario 3.1: Find Pets with Status "Available" (Positive)
Given I specify the status as "available"
When I send a GET request to /pet/findByStatus
Then The response status should be 200 OK
And The response body should contain a list of pets with status "available"

Scenario 3.2: Find Pets with an Invalid Status (Negative)
Given I specify an invalid status value
When I send a GET request to /pet/findByStatus
Then The response status should be 400 Bad Request
And The response should indicate an invalid status parameter
```

## 4. GET /pet/findByTags - Find Pets by Tags
```gherkin
Scenario 4.1: Find Pets by Valid Tag (Positive)
Given I specify a valid tag in the query parameters
When I send a GET request to /pet/findByTags
Then The response status should be 200 OK
And The response body should contain a list of pets with the specified tag

Scenario 4.2: Find Pets by Invalid Tag (Negative)
Given I specify a non-existent tag
When I send a GET request to /pet/findByTags
Then The response status should be 404 Not Found
And The response should indicate no pets were found
```

## 5. GET /pet/{petId} - Find Pet by ID
```gherkin
Scenario 5.1: Find a Pet with Valid ID (Positive)
Given I have a valid pet ID
When I send a GET request to /pet/{petId}
Then The response status should be 200 OK
And The response body should contain the pet's details

Scenario 5.2: Find a Pet with Invalid ID (Negative)
Given I have an invalid pet ID
When I send a GET request to /pet/{petId}
Then The response status should be 404 Not Found
And The response should indicate the pet was not found
```

## 6. POST /pet/{petId} - Update a Pet Using Form Data
```gherkin
Scenario 6.1: Update a Pet's Name Using Form Data (Positive)
Given I have a valid pet ID
When I send a POST request to /pet/{petId} with form data containing a new name
Then The response status should be 200 OK
And The response should confirm the pet was updated

Scenario 6.2: Update a Pet with Invalid Form Data (Negative)
Given I have a valid pet ID
When I send a POST request to /pet/{petId} with invalid form data
Then The response status should be 400 Bad Request
And The response should indicate a validation error
```

## 7. DELETE /pet/{petId} - Delete a Pet
```gherkin
Scenario 7.1: Delete a Pet with Valid ID (Positive)
Given I have a valid pet ID
When I send a DELETE request to /pet/{petId}
Then The response status should be 200 OK
And The response should confirm the pet was deleted

Scenario 7.2: Delete a Pet with Invalid ID (Negative)
Given I have an invalid pet ID
When I send a DELETE request to /pet/{petId}
Then The response status should be 404 Not Found
And The response should indicate the pet was not found
```

## 8. POST /pet/{petId}/uploadImage - Upload an Image
```gherkin
Scenario 8.1: Upload a Valid Image (Positive)
Given I have a valid pet ID
And I have a valid image file
When I send a POST request to /pet/{petId}/uploadImage
Then The response status should be 200 OK
And The response should confirm the image was uploaded

Scenario 8.2: Upload an Invalid File (Negative)
Given I have a valid pet ID
And I have an invalid file format
When I send a POST request to /pet/{petId}/uploadImage
Then The response status should be 400 Bad Request
And The response should indicate an invalid file format
```
