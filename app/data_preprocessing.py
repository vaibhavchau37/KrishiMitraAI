def validate_pincode(pincode):
    """
    Validate Indian PIN code format
    """
    if not pincode.isdigit() or len(pincode) != 6:
        raise ValueError("Invalid PIN code. Please enter a 6-digit number.")
    return pincode

def validate_land_area(land_area):
    """
    Validate land area input
    """
    if land_area <= 0:
        raise ValueError("Land area must be greater than 0 acres.")
    return land_area

def validate_budget(budget):
    """
    Validate budget input
    """
    if budget < 1000:
        raise ValueError("Budget must be at least ₹1,000.")
    return budget

def preprocess_user_input(pincode, land_area, budget):
    """
    Preprocess and validate user inputs
    """
    processed_input = {
        'pincode': validate_pincode(str(pincode)),
        'land_area': validate_land_area(float(land_area)),
        'budget': validate_budget(float(budget))
    }
    
    return processed_input
