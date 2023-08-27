#include <stdio.h>

int is_palindrome(char *str, char **str1)
{
	int result;

	if (*str == '\0')
	{
		return (1);
	}
	result = is_palindrome(str + 1, str1);

	printf("%c == %c\n", **str1, *str);

	if (**str1 != *str)
		return (0);

	(*str1)++;

	return result;


}


int main(void)
{
	char *s = "oo";


	int d = is_palindrome("oo", &s);
	printf("is_pal = %d\n", d);


	return (0);
}
