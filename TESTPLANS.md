# Test Plan for Testing Aridia ML

## Test Plan Overview

This test plan aims to validate the accuracy of Aridia ML in recognizing American Sign Language (ASL) signs, including static signs and those that require hand movements (e.g., the letter "Z"). The tests will ensure that the model accurately predicts sign letters by comparing the predicted output with the expected output for a given set of sign patterns.

## Test Setup

1. Ensure Python 3.12 or higher is installed.
2. Install dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the `test_model.py` script by executing:

   ```bash
   python -u test_model.py
   ```

4. Ensure camera permissions are granted when prompted.

## Test Cases

### Test Case 1: Single Letter Recognition

#### Objective

To verify if the model accurately recognizes individual ASL letters.

#### Test Steps

1. Run the `test_model.py` script.
2. Perform the ASL sign for a single letter (e.g., A).
3. Observe and record the predicted letter from the model.
4. Compare the predicted letter with the expected letter.

#### Expected Result

The model should correctly identify the ASL letter being signed.

### Test Case 2: Continuous Letter Recognition

#### Objective

To verify if the model can accurately recognize a sequence of ASL letters being signed continuously.

#### Test Steps

1. Run the `test_model.py` script.
2. Perform a sequence of ASL letters (e.g., A, B, C, D) continuously.
3. Observe and record the sequence of predicted letters from the model.
4. Compare the predicted sequence with the expected sequence.

#### Expected Result

The model should correctly identify each ASL letter in the sequence.

### Test Case 3: Variable Lighting Conditions

#### Objective

To verify if the model can accurately recognize ASL letters under different lighting conditions.

#### Test Steps

1. Run the `test_model.py` script.
2. Perform the ASL sign for a single letter under different lighting conditions (e.g., bright light, dim light, natural light).
3. Observe and record the predicted letter from the model for each condition.
4. Compare the predicted letters with the expected letters.

#### Expected Result

The model should correctly identify the ASL letter being signed under each lighting condition.

### Test Case 4: Background Noise

#### Objective

To verify if the model can accurately recognize ASL letters with various background noise levels.

#### Test Steps

1. Run the `test_model.py` script.
2. Perform the ASL sign for a single letter with different background noises (e.g., quiet background, moderate background noise, loud background noise).
3. Observe and record the predicted letter from the model for each noise level.
4. Compare the predicted letters with the expected letters.

#### Expected Result

The model should correctly identify the ASL letter being signed regardless of the background noise level.

### Test Case 5: Different Signers

#### Objective

To verify if the model can accurately recognize ASL letters signed by different individuals.

#### Test Steps

1. Run the `test_model.py` script.
2. Have different individuals perform the ASL sign for a single letter.
3. Observe and record the predicted letter from the model for each individual.
4. Compare the predicted letters with the expected letters.

#### Expected Result

The model should correctly identify the ASL letter being signed by each individual.

### Test Case 6: Hand Movements for Dynamic Signs

#### Objective

To verify if the model can accurately recognize ASL letters that require hand movements (e.g., the letter "Z").

#### Test Steps

1. Run the `test_model.py` script.
2. Perform the ASL sign for a letter that requires hand movement, such as "Z".
3. Observe and record the predicted letter from the model.
4. Compare the predicted letter with the expected letter.

#### Expected Result

The model should correctly identify the ASL letter being signed, even when it involves hand movement.
