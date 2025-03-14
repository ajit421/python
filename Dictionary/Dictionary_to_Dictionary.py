tea_shop = {
    "chai": {
        "Masala": "spicy",
        "Ginger": "Zesty",
        "Green": "Mild",
        "Black": "Strong"
    }, "tea": {
        "Earl Grey": "Citrus",
        "English Breakfast": "Robust",
        "Darjeeling": "Floral",
        "Jasmine": "Fragrant"
    }

}
print(tea_shop) # Output: {'chai': {'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'Mild', 'Black': 'Strong'}, 'tea': {'Earl Grey': 'Citrus', 'English Breakfast': 'Robust', 'Darjeeling': 'Floral', 'Jasmine': 'Fragrant'}}
print(tea_shop["chai"]) # Output: {'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'Mild', 'Black': 'Strong'}
print(tea_shop["tea"]) # Output: {'Earl Grey': 'Citrus', 'English Breakfast': 'Robust', 'Darjeeling': 'Floral', 'Jasmine': 'Fragrant'}

print(tea_shop["chai"]["Masala"]) # Output: spicy
print(tea_shop["tea"]["Jasmine"]) # Output: Fragrant
print(tea_shop["chai"]["Black"]) # Output: Strong