#I have created this file -Dishant
from django.http import HttpResponse
from django.shortcuts import render
import re

def index(request):
    return render(request, 'index.html')
    
def aboutus(request):
    return render(request, 'aboutus.html')


def analyze(request):

    #! Got the text 
    djtext = request.POST.get('text', '')
    if not djtext.strip():
        return render(request, 'error1.html')

    #! Accsing the function which is on / off
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    propercase = request.POST.get('propercase', 'off')
    sentencecase = request.POST.get('sentencecase', 'off')
    trim = request.POST.get('trim', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')


    #! Performing the desired function

    # List of proper nouns (add more as needed)
    proper_nouns = [
        "American","Afghanistan", "Argentina", "Australia", "Brazil", "Canada", "China", 
        "Egypt", "France", "Germany", "India", "Italy", "Japan", "Mexico", 
        "Russia", "South Africa", "United Kingdom", "United States", 
        "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
        "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Francisco", 
        "London", "Paris", "Berlin", "Tokyo", "Beijing", "Sydney", "Mumbai", 
        "Cairo", "Rio de Janeiro", "John", "Mary", "Robert", "Patricia", 
        "Michael", "Linda", "William", "Elizabeth", "David", "Jennifer", 
        "James", "Maria", "Charles", "Susan", "Christopher", "Karen", 
        "Daniel", "Sarah", "Apple", "Microsoft", "Google", "Amazon", "Facebook", 
        "Tesla", "Samsung", "IBM", "Coca-Cola", "Pepsi", "Nike", "Adidas", 
        "Sony", "Toyota", "Ford", "BMW", "McDonald's", "Starbucks", 
        "Mount Everest", "Nile River", "Sahara Desert", "Amazon Rainforest", 
        "Great Barrier Reef", "Rocky Mountains", "Himalayas", "Pacific Ocean", 
        "Atlantic Ocean", "Mediterranean Sea", "Statue of Liberty", "Eiffel Tower", 
        "Great Wall of China", "Pyramids of Giza", "Colosseum", "Taj Mahal", 
        "Machu Picchu", "Louvre Museum", "Sydney Opera House", "Big Ben", 
        "United Nations", "World Health Organization", "NASA", "Harvard University", 
        "Stanford University", "Oxford University", "MIT", "World Bank", "IMF", 
        "Red Cross", "Christmas", "Thanksgiving", "New Year's Day", "Independence Day", 
        "Easter", "Halloween", "Hanukkah", "Ramadan", "Diwali", "Olympics", "World Cup", 
        "Harry Potter", "The Lord of the Rings", "The Great Gatsby", "To Kill a Mockingbird", 
        "Star Wars", "The Godfather", "Game of Thrones", "The Matrix", "Inception", "Titanic"
    ]

    if (removepunc == "off" and 
    uppercase == "off" and 
    lowercase == "off" and 
    propercase == "off" and 
    sentencecase == "off" and 
    trim == "off" and 
    newlineremover == "off"):
    
        return render(request, 'error2.html')
    
    
    
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed+char
        djtext=analyzed
    
    if(uppercase=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed+char.upper()
        djtext=analyzed
    
    if(lowercase=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed+char.lower()
        djtext=analyzed
    
    if(propercase=="on"):
        analyzed=djtext
        for char in djtext:
            analyzed = djtext.title()
        djtext=analyzed
    
    if sentencecase == "on":
        # Convert to sentence case
        sentences = re.split('([.!?] *)', djtext.lower())
        analyzed = ''.join([s.capitalize() for s in sentences])
        
        # Capitalize known proper nouns
        for proper_noun in proper_nouns:
            analyzed = re.sub(r'\b{}\b'.format(proper_noun.lower()), proper_noun, analyzed)
        djtext = analyzed

    if(trim=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed+char
        djtext=analyzed
    
    if(newlineremover=="on"):
        analyzed = djtext.translate({ord('\n'): None, ord('\r'): None})
        djtext=analyzed
    
    # Calculate character count after all operations
    char_count = len(djtext)

    # Calculate word count after all operations
    word_count = len(djtext.split())

    

    # Prepare the final parameters
    params = {
        'purpose': 'Text Analysis',
        'analyzed_text': djtext,
        'charcater_count': char_count,
        'word_count':word_count
    }
    
    return render(request, 'analyze.html', params)

    


