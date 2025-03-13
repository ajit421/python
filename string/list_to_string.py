chai_variety = ['Masala', 'Ginger', 'Green', 'Kashmiri']
print(chai_variety) # Output: ['Masala', 'Ginger', 'Green', 'Kashmiri']

print("".join(chai_variety)) # Output: 'MasalaGingerGreenKashmiri'

print(", ".join(chai_variety)) # Output: 'Masala, Ginger, Green, Kashmiri'

print("-".join(chai_variety)) # Output: 'Masala-Ginger-Green-Kashmiri'

print(" & ".join(chai_variety)) # Output: 'Masala & Ginger & Green & Kashmiri'

print(" or ".join(chai_variety)) # Output: 'Masala or Ginger or Green or Kashmiri'

print(" and ".join(chai_variety)) # Output: 'Masala and Ginger and Green and Kashmiri'

print("".join(chai_variety).replace('Masala', 'Kashmiri')) # Output: 'KashmiriGingerGreenKashmiri'

print(", ".join(chai_variety).replace('Masala', 'Kashmiri')) # Output: 'Kashmiri, Ginger, Green, Kashmiri'

