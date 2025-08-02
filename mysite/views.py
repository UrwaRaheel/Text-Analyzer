from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        analyzed = text
        actions = []

        # Remove punctuation
        if request.POST.get('remove_punc'):
            analyzed = ''.join(char for char in analyzed if char.isalnum() or char.isspace())
            actions.append("Removed Punctuation")

        # Capitalize text
        if request.POST.get('capitalize'):
            analyzed = analyzed.upper()
            actions.append("Capitalized Text")

        # Remove extra spaces
        if request.POST.get('remove_space'):
            import re
            analyzed = re.sub(r'\s+', ' ', analyzed).strip()

            actions.append("Removed Extra Spaces")

        char_count = len(analyzed)
        word_count = len(analyzed.split())

        context = {
            'analyzed_text': analyzed,
            'actions': actions,
            'char_count': char_count,
            'word_count': word_count,
        }
        return render(request, 'analyze.html', context)

    else:
        return render(request, 'index.html')
