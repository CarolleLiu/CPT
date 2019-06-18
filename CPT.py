count_wrong_answer = 0
print("                                                                                  ")

print("                           Computer science Quiz")
print("                                                                                  ")
print("                    Welcome to the Computer science Quiz !")
print("                                                                               ")
print("                This quiz will be based on some of the context ")
print("                taught in ICS201 and some context relating with ")
print("                      computers and society. Good Luck!  ")
print("                                                                                  ")
print("                                                                                  ")


print("1. What is the 8th largest measurement of storage? ")
print("   a. Yottabyte ")
print("   b. Treabyte ")
print("   c. Exabyte ")
print("   d. Zettabyte ")

print("                                                                                  ")

answer = "c"

choice = input("Choose option a, b, c or d: ")

while choice != "a" and choice != "b" and choice != "c" and choice != "d":
    print("Wrong answer :( Try again.")
    choice = input("Choose option a, b, c or d: ")

if choice == "a" or choice == "b" or choice == "d":
    count_wrong_answer += 1
    print("Wrong Answer, but moving on")
    print('                                                                               ')
elif choice == "c":
    print('Nice Job! Next Question')
    print('                                                                               ')

print("2. What is the smallest unit of measurement? ")
print("   a. Bytes ")
print("   b. Bit ")
print("   c. Megabit ")
print("   d. Megabyte ")

print("                                                                                  ")

answer = "b"

choice = input("Choose option a, b, c or d: ")

while choice != "a" and choice != "b" and choice != "c" and choice != "d":
    print("Wrong answer :( Try again.")
    choice = input("Choose option a, b, c or d: ")

if choice == "a" or choice == "c" or choice == "d":
    count_wrong_answer += 1
    print("Wrong Answer, but moving on")
    print('                                                                               ')
elif choice == "b":
    print('Nice Job! Next Question')
    print('                                                                               ')

print("3. How can one of the options listed help to improve the safety of your computer?")
print("   a. More internal storage ")
print("   b. Better graphics card ")
print("   c. Long lasting power supply ")
print("   d. None of the above ")

print("                                                                                  ")

answer = "d"

choice = input("Choose option a, b, c or d: ")

while choice != "a" and choice != "b" and choice != "c" and choice != "d":
        print("Wrong answer :( Try again.")
        choice = input("Choose option a, b, c or d: ")

if choice == "a" or choice == "b" or choice == "c":
    count_wrong_answer += 1
    print("Wrong Answer, but moving on")
    print('                                                                               ')
elif choice == "d":
    print('Nice Job! Next Question')
    print('                                                                               ')

print("4. What is the average amount of RAM in recent laptop models? ")
print("   a. 8GB ")
print("   b. 4GB ")
print("   c. 16GB ")
print("   d. 32GB ")

print("                                                                                  ")

answer = "a"

choice = input("Choose option a, b, c or d: ")

while choice != "a" and choice != "b" and choice != "c" and choice != "d":
        print("Wrong answer :( Try again.")
        choice = input("Choose option a, b, c or d: ")

if choice == "d" or choice == "b" or choice == "c":
    count_wrong_answer += 1
    print("Wrong Answer, but moving on")
    print('                                                                               ')
elif choice == "a":
    print('Nice Job! Next Question')
    print('                                                                               ')

print("5. Which of the following in a network encourages our daily technology addictions?  ")
print("   a. ISP ")
print("   b. The internet ")
print("   c. Modem ")
print("   d. Extender ")

print("                                                                                  ")

answer = "b"

choice = input("Choose option a, b, c or d: ")

while choice != "a" and choice != "b" and choice != "c" and choice != "d":
        print("Wrong answer :( Try again.")
        choice = input("Choose option a, b, c or d: ")

if choice == "d" or choice == "a" or choice == "c":
    count_wrong_answer += 1
    print("Wrong Answer, but moving on")
    print('                                                                               ')
elif choice == "b":
    print('Nice Job! Next Question')
    print('                                                                               ')

print("6. An extender extends the distance over which a WLAN signal can spread. What is a WLAN (Wireless LAN) ?")
print("   a. A wireless computer network that links two or more devices using wireless communication to form a local area network within a limited area ")
print("   b. A global computer network providing a variety of information and communication facilities, consisting of interconnected networks using standardized communication protocols ")
print("   c. Converts data into a format suitable for transmission medium so that it can be transmitted from computer to computer ")
print("   d. A hardware device or software program that protects your network from malicious users and offensive Websites, keeping hackers from accessing or destroying your data. ")

print("                                                                                  ")

answer = "a"

choice = input("Choose option a, b, c or d: ")

while choice != "a" and choice != "b" and choice != "c" and choice != "d":
        print("Wrong answer :( Try again.")
        choice = input("Choose option a, b, c or d: ")

if choice == "d" or choice == "b" or choice == "c":
    count_wrong_answer += 1
    print("Wrong Answer, but moving on")
    print('                                                                               ')
elif choice == "a":
    print('Nice Job! Next Question')
    print('                                                                               ')

print("7. Which of the following malware duplicates itself and destroys data ")
print("   a. Rootkit ")
print("   b. Browser hijakcer ")
print("   c. Backdoor ")
print("   d. Worm ")

print("                                                                                  ")

answer = "d"

choice = input("Choose option a, b, c or d: ")

while choice != "a" and choice != "b" and choice != "c" and choice != "d":
        print("Wrong answer :( Try again.")
        choice = input("Choose option a, b, c or d: ")

if choice == "a" or choice == "b" or choice == "c":
    count_wrong_answer += 1
    print("Wrong Answer, but moving on")
    print('                                                                               ')
elif choice == "d":
    print('Nice Job! Next Question')
    print('                                                                               ')

print("8. Which of the following would NOT help to prevent your computer from ransomware? ")
print("   a. Use a firewall ")
print("   b. Keep personal information saved on browsers  ")
print("   c. Download anti-virus ")
print("   d. Manual system resets ")

print("                                                                                  ")

answer = "b"

choice = input("Choose option a, b, c or d: ")

while choice != "a" and choice != "b" and choice != "c" and choice != "d":
        print("Wrong answer :( Try again.")
        choice = input("Choose option a, b, c or d: ")

if choice == "a" or choice == "d" or choice == "c":
    count_wrong_answer += 1
    print("Wrong Answer, but moving on")
    print('                                                                               ')
elif choice == "b":
    print('Nice Job! Next Question')
    print('                                                                               ')

print("9. Which of the following ways do NOT improve our society through computers? ")
print("   a. Expanded our ability to socialize on a larger scale, in vast distances ")
print("   b. Help with shopping/ gave the convenience of shopping/purchasing objects online ")
print("   c. computer links us to the society, giving easier access and ability if to cyberbully ")
print("   d. Improve organization ")

print("                                                                                  ")

answer = "c"

choice = input("Choose option a, b, c or d: ")

while choice != "a" and choice != "b" and choice != "c" and choice != "d":
        print("Wrong answer :( Try again.")
        choice = input("Choose option a, b, c or d: ")

if choice == "a" or choice == "b" or choice == "d":
    count_wrong_answer += 1
    print("Wrong Answer, but moving on")
    print('                                                                               ')
elif choice == "c":
    print('Nice Job! Next Question')
    print('                                                                               ')

print("10. Computers have helped our society in many ways ")
print("   a. True ")
print("   b. False ")

print("                                                                                  ")

answer = "a"

choice = input("Choose option a or b: ")

if choice == "a" or choice == "b":
    count_wrong_answer += 1
    print("Wrong Answer, but moving on")
    print('                                                                               ')
elif choice == "a":
    print('Nice Job! Next Question')
    print('                                                                               ')
else:
    print("Wrong answer :( Try again.")
    choice = input("Choose option a, b, c or d: ")

print("11. In what ways do computers negatively affect our environment? ")
print("   a. By going on many web browsers, we strain our eyes ")
print("   b. Computers are made out of heavy metals which are extremely harmful when thrown into the ocean ")
print("   c. We can order food online resulting in the build up of indolence ")

print("                                                                                  ")

choice = input("Choose option a, b, c or d: ")

answer = "b"

if choice == "c" or choice == "a" or choice == "d":
    count_wrong_answer += 1
    print("Wrong Answer, but moving on")
    print('                                                                               ')
elif choice == "b":
    print('Nice Job! Next Question')
    print('                                                                               ')
else:
    print("Wrong answer :( Try again.")
    choice = input("Choose option a, b, c or d: ")

print("12. How can we improve or reduce negative effects of computers on our environment? ")
print("   a. When you want to rid yourself of an old computer, deliver it to a recycling company so it can be disposed of properly ")
print("   b. Never talk with anyone again on Facebook, Skype, Discord, etc. ")
print("   c. There are no negative effects of computers on your environment ")
print("   d. All of the above ")

print("                                                                                  ")

choice = input("Choose option a, b, c or d: ")

answer = "a"

if choice == "c" or choice == "b" or choice == "d":
    count_wrong_answer += 1
    print("Wrong Answer, but moving on")
    print('                                                                               ')
elif choice == "a":
    print('Nice Job! Next Question')
    print('                                                                               ')
else:
    print("Wrong answer :( Try again.")
    choice = input("Choose option a, b, c or d: ")

print("13. Which of the following questions below may be an ethical question? ")
print("   a. Are computers a good investment for you? ")
print("   b. Are computers beneficial to your health? ")
print("   c. Is copying software and applications a form of stealing? ")

print("                                                                                  ")

choice = input("Choose option a, b, c or d: ")

answer = "c"

if choice == "a" or choice == "b" or choice == "d":
    count_wrong_answer += 1
    print("Wrong Answer, but moving on")
    print('                                                                               ')
elif choice == "c":
    print('Nice Job! Next Question')
    print('                                                                               ')
else:
    print("Wrong answer :( Try again.")
    choice = input("Choose option a, b, c or d: ")

print("14. What is not included in ethical issues regarding computers? ")
print("   a. Privacy ")
print("   b. Copying Software ")
print("   c. Playing games ")
print("   d. None of the above ")

print("                                                                                  ")

choice = input("Choose option a, b, c or d: ")

answer = "c"

if choice == "a" or choice == "b" or choice == "d":
    count_wrong_answer += 1
    print("Wrong Answer, but moving on")
    print('                                                                               ')
elif choice == "c":
    print('Nice Job! Next Question')
    print('                                                                               ')
else:
    print("Wrong answer :( Try again.")
    choice = input("Choose option a, b, c or d: ")

print("15. What is a possible prerequisite for entering university/college majoring in computer science? ")
print("   a. Calculus, English, Physics, Advanced Functions ")
print("   b. Music, English, Religion and Advanced Functions ")
print("   c. Art, Biology, Religion and Physics ")
print("   d. Data Management, Chemistry, Photography and Music ")

print("                                                                                  ")

choice = input("Choose option a, b, c or d: ")

answer = "a"

if choice == "c" or choice == "b" or choice == "d":
    count_wrong_answer += 1
    print("Wrong Answer, but moving on")
    print('                                                                               ')
elif choice == "a":
    print('Nice Job! Next Question')
    print('                                                                               ')
else:
    print("Wrong answer :( Try again.")
    choice = input("Choose option a, b, c or d: ")

print("                                                                                  ")

print("    Congratulations! You have completed the multiple choice Computer Science Quiz.")

print("                                                                                  ")

print("                        You had " + str(count_wrong_answer) + " failed attempts.")