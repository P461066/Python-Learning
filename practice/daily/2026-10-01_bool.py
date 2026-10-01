# Driving Eligibility Checker
# step 1: Define the variables
has_licence = True
has_experience = True
has_record = True
disc_expired = False

# step 2: Check the conditions for driving eligibility
can_drive = has_licence and has_experience and not has_record and not disc_expired
cannot_drive = not has_licence or not has_experience or has_record or disc_expired
banned =has_licence and (has_record or disc_expired)
not_permitted = not has_licence or not has_experience  or has_record or disc_expired

# step 3: Print the results
if can_drive:
    print("You are eligible to drive.")
elif cannot_drive:
    print("You are not eligible to drive.")    
elif banned:
    print("You are banned from driving. check your record or license status.")
else:
    print("You are not permitted to drive. Please check apply for a license and get experience.")
