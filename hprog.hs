--use System.Environment to be able to take user input
import System.Environment
--DAY 1
--subtracts each element of a list by 1
-- subtractBy1 :: [Int] ->[Int]
-- subtractBy1 [] = []
-- subtractBy1(x:xs) = (x - 1) : subtractBy1 xs

--subtract each element from 255
invertPixelValue :: [Int] -> [Int]
invertPixelValue [] = []
invertPixelValue (x:xs) = (255-x) : invertPixelValue xs

--main I/O function
main :: IO()
main = do 
    args <- getArgs 
    --command line args are collected as a string

    --use inbuilt read function to convert string to int
    -- ::[Int] is the type signature
    let numbers = map read args :: [Int]

    --call the function
        result = invertPixelValue numbers 

    --convert the result back to a tsring
        resultString = map show result 
        outputString = unwords resultString

    --print the string
    putStrLn outputString 


