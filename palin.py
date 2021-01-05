# 펠린드롭 01
def is_palindrome1(word):
    word = list(word)
    reverse = word[-1: : -1]
    return word == reverse

# 펠린드롭 02
def is_palindrome2(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False
    # for문에서 나왔다면 모든 쌍이 일치
    return True
# 테스트
print(is_palindrome1("racecar"))
print(is_palindrome1("stars"))
print(is_palindrome2("토마토"))
print(is_palindrome2("kayak"))
print(is_palindrome1("hello"))