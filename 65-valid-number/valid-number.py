class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return False

        def is_integer(string):
            if not string:
                return False
            if string[0] in ['+', '-']:
                string = string[1:]
            return string.isdigit()

        def is_decimal(string):
            if not string:
                return False
            if string[0] in ['+', '-']:
                string = string[1:]

            if '.' not in string:
                return False

            before_dot, after_dot = string.split('.', 1)
            # Allow empty before or after the dot, but not both
            if before_dot == '' and after_dot == '':
                return False
            if before_dot != '' and not before_dot.isdigit():
                return False
            if after_dot != '' and not after_dot.isdigit():
                return False
            return True

        # Split into base and exponent if 'e' or 'E' is found
        if 'e' in s or 'E' in s:
            parts = s.lower().split('e')
            if len(parts) != 2:
                return False
            base, exp = parts
            return (is_integer(base) or is_decimal(base)) and is_integer(exp)
        else:
            return is_integer(s) or is_decimal(s)