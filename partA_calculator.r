#CA5 R functions, 10359541 Seungmin Back

#1. Add
Add <- function(x,y) {
  result <- x+y
  print(paste(x,"add", y, "is", result))
}
Add(8,2)

#2. Subtract
Subtract <- function(x,y) {
  result <- x-y
  print(paste(x,"subtract", y, "is", result))
}
Subtract(8,2)

#3. Multiply
Multiply <- function(x,y) {
  result <- x*y
  print(paste(x,"multiply", y, "is", result))
}
Multiply(8,2)

#4. Divide
Divide <- function(x,y) {
  result <- x/y
  print(paste(x,"divide", y, "is", result))
}
Divide(8,2)

#5. Exponent
Exponent <- function(x,y) {return(x**y)}
print(Exponent(2,3))

#6. Square
Square <- function(x) {return(x^2)}
print(Square(4))

a = c(1,2,3,4,5)
print(Square(a))

#7. Square root
Square_root <- function(x) {return(x^0.5)}
print(Square_root(9))

#8. Factorial
Factorial <- function(x) {
  if(x <= 1) {
    return(1)
  } else {
    return(x * Factorial(x-1))
  }
}
print(Factorial(5))

#9. Sum
Sum_of_natural_numbers <- function(x) {
  if(x <=1) {
    return(x)
  } else {
    return(x+Sum_of_natural_numbers(x-1))
  }
}
print(Sum_of_natural_numbers(7))

#10. Odd or Even
Odd_or_even <- function(x) {
  x = as.integer(readline(prompt="Enter a number: "))
  if((x %% 2) == 0) {
    print(paste(x,"is Even"))
  } else {
    print(paste(x,"is Odd"))
  }
}

Odd_or_even(7)