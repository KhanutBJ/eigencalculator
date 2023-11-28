### App ##

import streamlit as st
import numpy as np
import cmath


st.title("Eigenvalue Calculator App")
st.title("Made by the two goats of RAMA")
st.write("---")

st.write("output: eigenvalues, eigenvectors, graph type")

st.write("limitation: cannot calculate eigenvector for imaginary part (i) TT")
st.write("disclaimer: We accept no responsibility or liability for any error in your score !")

def display_matrix(matrix, title):
    st.write(f"## {title}")
    for row in matrix:
        st.text(row)

def main():

    matrix_a = np.array([["First number", "Second number"],
                         ["Third number", "Fourth number"]])

    display_matrix(matrix_a, "Matrix Format")

if __name__ == "__main__":
    main()
    
    
num1 = st.number_input(label="Enter first number", value=None)
num2 = st.number_input(label="Enter second number", value=None)
num3 = st.number_input(label="Enter third number", value=None)
num4 = st.number_input(label="Enter fourth number", value=None)
 
ans = 0

from sympy import symbols, sqrt, factorint

def symbolic_square_root(n):
    x = symbols('x')
    return sqrt(n).rewrite(sqrt, x**(1/max(factorint(n).values(), default=1)))
 
def calculate():

    matrix = [[num1, num2],
              [num3, num4]]

    # Calculate eigenvalues and eigenvectors manually
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    st.write("Eigenvalues")
    root = np.power(num1+num4,2) - 4*np.linalg.det(matrix)
    
    if  root >= 0:
        values = np.array(eigenvalues).astype(int)
        st.success(f"Eigenvalues: {values[0]}, {values[1]} ")
    else:           
        try:
            result = symbolic_square_root(int(np.linalg.det(matrix)))
            x = f"+/- {result}i"
        except:
            result = cmath.sqrt(root)
            x = f"{result.imag/2}i"
        st.success(f"lambda: {(num1+num4) / 2} +/- mu: {x}")
    
    st.write("Eigenvectors")
    for i, eigenvector in enumerate(eigenvectors.T):
        n = 1
        try:
            while not np.all(np.modf(eigenvector)[0] == 0):
                eigenvector = [n* (x/np.max(eigenvector)) for x in eigenvector]
                n += 1
            st.success(f"Eigenvector for {int(eigenvalues[i])}: {np.array(eigenvector).astype(int)}")
        except:
            st.success("Sorry, too hard XD")
            break
    
    st.write("Type")
    
    if root < 0:
        lamb = (num1+num4) / 2
        if lamb == 0:
            st.success("center,stable")   
        elif lamb > 0:
            st.success("spiral,unstable")   
        elif lamb < 0:
            st.success("spiral,linear stable")   
    else: 
        if eigenvalues[0] != eigenvalues[1]:
            if eigenvalues[0] > 0 and eigenvalues[1] < 0:
                st.success("saddle,unstable")
            elif eigenvalues[1] > 0 and eigenvalues[0] < 0:
                st.success("saddle,unstable")
            elif eigenvalues[0] > 0 and eigenvalues[1] > 0:
                st.success("node,unstable")
            elif eigenvalues[0] < 0 and eigenvalues[1] < 0:
                st.success("node,linear stable")
        else:
            if matrix == np.array([[eigenvalues[0], 0],
                                    [0, eigenvalues[1]]]):
                if eigenvalues[0] > 0:
                    st.success("true node,unstable")
                else:
                    st.success("true node,linear stable")
            else:
                if eigenvalues[0] > 0:
                    st.success("fake node,unstable")
                else:
                    st.success("fake node,linear stable")

 
if st.button("Calculate result"):
    calculate()
 












