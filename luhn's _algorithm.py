from re import match

NUMBER_TO_MULTIPLY = 2
REGEX_BASIC_PATTER_CC = '([\d]+[- ]?[\d]+)+$'

# IT IS ALL INSIDE OF LIST, IN CASE THERE ARE MORE LEN/START VALUES. SO IN THE FUTURE WILL BE EASY TO MODIFY.   
CREDIT_CARDS = {"american_express":{"len":[15],"start_numbers":[34,37]},"mastercard":{"len":[16],"start_numbers":[51, 52, 53, 54,55]},
                "visa":{"start_numbers":[4],"len":[13,16]}}

class Valid_credit_card(object):
    
    def __init__(self,credit_card:object) -> None:
        """
        @param credit_card: It could be an int or a str.
        """
        self.__credit_card = credit_card

    def __luhn_algorithm(self) -> bool:
        """
        Through luhn algorithm, check if the credit card pass the first test to be valid.
        @raise Exception: If the given credit card can't pass basic test for validation.
        @return bool: It is valid for luhn's algorithm.
        """
        respect = self.__does_respect_basic_pattern()
        if respect:
            has_hyphens = self.__check_if_it_has_hypens()
            if has_hyphens:
                self.__credit_card = self.__replace_hyphen()
            elif self.__check_if_it_has_whitespaces():
                self.__credit_card = self.__replace_whitespaces()
            sum = 0
            sum_mul = 0
            i = len(self.__credit_card) - 1
            beyond_final_number = False
            while not beyond_final_number:
                #THERE ARE TWO OPPORTUNITIES WHERE I CAN BE LESS THAN 0.
                exceeded = i < 0
                if exceeded:
                    beyond_final_number = True
                else:
                    sum += int(self.__credit_card[i])
                    i -= 1
                    exceeded = i < 0
                    if exceeded:
                        beyond_final_number = True
                    else:
                        sum_mul += self.__obtain_sum_product_digits(self.__convert_into_int((self.__credit_card[i])),NUMBER_TO_MULTIPLY)  
                        i -= 1
            final_sum = sum + sum_mul
            valid = self.__ends_with_zero(final_sum)
        else:
            raise Exception(f"\nERROR: The credit card given don't respect basic pattern to be valid.\n")
        return valid

    def __does_respect_basic_pattern(self) -> bool:
        """
        Check if respect basic regex pattern for a credit card.
        I.e., if its number/s followed by a - or ' ' and then follow by number/s again.
        Like this, n amount of times. 
        @return bool: If respects. return True, false otherwise.
        """
        is_str = self.__is_it_a_str()
        if not is_str:
            self.__credit_card = self.__convert_into_str(self.__credit_card)
        return match(REGEX_BASIC_PATTER_CC,self.__credit_card)

    def __check_if_it_has_whitespaces(self) -> bool:
        """
        Check if it has whitespaces.
        @return bool: If it has, return True; false otherwise.
        """
        return " " in self.__credit_card

    def __replace_whitespaces(self) -> str:
        """
        Replace whitespaces with "".
        @return str: The credit card without whitespaces.
        """
        return self.__credit_card.replace(" ","")

    def __replace_hyphen(self) -> str:
        """
        Replace hyphen/s with "".
        @return str: The credit card without hyphen/s.
        """
        return self.__credit_card.replace("-","")


    def __check_if_it_has_hypens(self) -> bool:
        """
        Check if it has hypens.
        @return bool: If it has, return True; false otherwise.
        """
        return "-" in  self.__credit_card

    
    def __is_it_a_str(self) -> bool:
        """
        Check if the credit_card given is a str.
        @return bool: Return True if it is an instance of str, false otherwise.
        """
        return isinstance(self.__credit_card,str)

    def __ends_with_zero(self,final_sum:int) -> bool:
        """
        Check if the last number is zero.
        @param final_sum: The result of all the sums in the algorithm.
        @return bool: True if it ends with zero, false otherwise.
        """
        ends_with_zero = final_sum % 10 == 0
        if ends_with_zero:
            valid = True
        else:
            valid = False
        return valid 

    def __obtain_sum_product_digits(self,digit:int,n_multiply:int) -> int:
        """
        Multiply number received with constant to multuply.
        Check if the result is a two digits number.
        If that is the case, then take different steps that if\n
        it is a one digit number.
        @param digit: The digit to be multiply.
        @param n_multiply: The constant wich the digit will be multiply.
        @return sum: The result of the multiplication or the sum of the result of the multiplication.
        """
        mul = digit * n_multiply
        two_digits = mul >= 10
        if two_digits:
            sum = self.__obtain_add_product_digits(mul)
        else:
            sum = mul
        return sum

    def __obtain_add_product_digits(self,digits:int) -> int:
        """
        Receives a number bigger than 9. Convert to str to separete it.
        And then, convert those two new variables in int. Hence, it can be add.
        @param mul: A number of two digits.
        @return sum: The sum of the two digits.
        """
        str_digits = self.__convert_into_str(digits)
        digit_one = self.__convert_into_int(str_digits[0])
        digit_two = self.__convert_into_int(str_digits[1])
        return digit_one + digit_two

    def __convert_into_int(self,string:str) -> int:
        """
        Convert string to int.
        @param string: String to be convert into int.
        @return int: The string converted into int.
        """
        return int(string)

    def __convert_into_str(self,num:int) -> str:
        """
        Convert number int str:
        @param num: Number to convert.
        @return str: The number converted.
        """
        return str(num)
    
    def validate_credit_card(self) -> None:
        """
        """
        response = self.__luhn_algorithm()
        if response:
            its_visa = self.__it_is_visa()
            if its_visa:
                self.__final_answer("VISA")
            elif self.__it_is_mastercard():
                self.__final_answer("Mastercard")  
            elif self.__it_is_american_express():
                self.__final_answer("American Express") 
            else:
                self.__possible_explanation()
        else:
            print("It is not a credit card.\nFails luhn algorithm -_-.")

    def __it_is_visa(self) -> bool:
        """
        Check if the credit card is visa.
        @return bool: True if it is visa, false otherwise.
        """
        valid_len = len(self.__credit_card) in CREDIT_CARDS["visa"]["len"]
        valid_start_number = int(self.__credit_card[0]) in CREDIT_CARDS["visa"]["start_numbers"]
        return valid_len and valid_start_number

    def __it_is_mastercard(self)-> bool:
        """
        Check if the credit card is mastercard.
        @return bool: True if it is mastercard, false otherwise.
        """
        valid_len = len(self.__credit_card) in CREDIT_CARDS["mastercard"]["len"]
        two_first_numbers = self.__obtain_two_first_numbers_as_int() 
        valid_start_number = two_first_numbers in CREDIT_CARDS["mastercard"]["start_numbers"]
        return valid_len and valid_start_number

    def __it_is_american_express(self) -> bool:
        """
        Check if the credit card is American Express.
        @return bool: True if it is American Express, false otherwise."
        """
        valid_len = len(self.__credit_card) in CREDIT_CARDS["american_express"]["len"]
        two_first_numbers = self.__obtain_two_first_numbers_as_int() 
        valid_start_number = two_first_numbers in CREDIT_CARDS["american_express"]["start_numbers"]
        return valid_len and valid_start_number


    def __obtain_two_first_numbers_as_int(self) -> int:
        """
        Obtain two first numbers of credit card (str).
        Ann return them as an int.
        @return two_first_numbers: The two first numbers, type int.
        """
        two_first_numbers = self.__credit_card[0] + self.__credit_card[1]
        two_first_numbers = self.__convert_into_int(two_first_numbers)
        return two_first_numbers

    def __final_answer(self,sign:str) -> None:
        """
        This method is responsable for inform the usser what kind of credit card is.
        @param sign: The type of credit card. 
        """ 
        print(f"\n{'*'*20}{self.__credit_card}{'*'*20}")
        print(f"The credit card is: {sign}")

    def __possible_explanation(self) -> None:
        """
        Explain the different scenarios of why the credit card that is valid,\n
        for the script it is not.
        """
        print(f"\n{'*'*20}{self.__credit_card}{'*'*20}")
        sign = """
It could happen three scenarios:

First one: The number don't belong to any company.

Second one: It is valid and belongs to one of the companies acquaintance in the script,\n
            but it is not updated.

Third one: It is valid and belongs to another company that is not acquaintance in the script.
"""
        print(sign)

def enter_cc() -> str:
    """
    Enter credit card or stop.
    """
    return str(input("Enter credit card or exit (i.e., 'N' = no): "))

def stop(string:str) -> bool:
    """
    Check if the program must stop or not.
    @param string: String to check.
    @return bool: If string is 'N', return Tru; false otherwise.
    """
    return string == 'N' 

def main():
    keep_asking = True
    while keep_asking:
        cc = enter_cc()
        condition = stop(cc)
        if condition:
            keep_asking = False
            print("Thanks for passing!")
        else:
            Valid_credit_card(cc).validate_credit_card()

main()