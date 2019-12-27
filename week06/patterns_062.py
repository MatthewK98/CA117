from re import findall
import sys

date = r"\d{1,2}[/-]\d{1,2}[-/]\d{1,2}"
phone = r"[0][1][\s-]\d{7}"
email = r"[a-z|.]*[@][a-z+.]+[a-z]"
ldate = r"\d{1,2}[\s](?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[\s]\d{1,2}"

def main():

    # Verify regular expressions are not overly long
    assert(len(date) < 30)
    assert(len(phone) < 30)
    assert(len(email) < 40)
    assert(len(ldate) < 80)

    s = sys.stdin.read()

    datelist = findall(date, s)
    print('Dates: {}'.format(datelist))

    phonelist = findall(phone, s)
    print('Phones: {}'.format(phonelist))

    emaillist = findall(email, s)
    print('Emails: {}'.format(emaillist))

    ldatelist = findall(ldate, s)
    print('Long dates: {}'.format(ldatelist))

if __name__ == '__main__':
    main()
