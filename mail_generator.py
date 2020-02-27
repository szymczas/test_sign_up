import random
import string

domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase[:24]

def generator_numbers():
    return str(random.randint(100, 999))


def get_random_domain(domains):
       return random.choice(domains)

def get_random_name(letters, length):
       return ''.join(random.choice(letters) for i in range(length))

def generate_random_emails(nb, length):
       return ["szdazn+" + get_random_name(letters, length) + generator_numbers() + '@' + get_random_domain(domains) for i in range(nb)]

def main():
    print(generate_random_emails(1, 3))


if __name__ == "__main__":
       main()
