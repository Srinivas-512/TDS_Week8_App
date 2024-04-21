import streamlit as st

def find_largest(a, b, c):
    return max(a, b, c)

def main():
    st.title('Find the Largest Number')
    
    st.write("Enter three numbers below to find the largest among them.")
    
    number1 = st.number_input("Enter the first number:", value=0)
    number2 = st.number_input("Enter the second number:", value=0)
    number3 = st.number_input("Enter the third number:", value=0)
    
    if st.button("Find Largest"):
        largest = find_largest(number1, number2, number3)
        st.write(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
