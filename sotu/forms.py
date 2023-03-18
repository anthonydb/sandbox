import datetime
from sotu.models import Speech
from django.shortcuts import render
from django import forms
from django.forms import ModelForm, Textarea


class SearchForm(ModelForm):
    """
    Form for searching president's speeches.
    """
    text_to_search = forms.CharField(label='Search terms (put phrases in quotes; exclude a word by prepending a hyphen)',
                            widget=Textarea(attrs={'cols': 50, 'rows': 1})
                            )
    president_to_search = forms.CharField(label='President (any part of a name)', required=False, 
                            widget=Textarea(attrs={'cols': 50, 'rows': 1})
                            )
    date_from = forms.DateField(label='From (yyyy-mm-dd)', initial='1940-01-01')
    date_through = forms.DateField(label='To (yyyy-mm-dd)', initial=datetime.date.today)

    class Meta:
        model = Speech
        # The below list needs to include all fields in the model.
        exclude = ['speech_date', 'speech_text', 'search_speech_text', 'title', 'president']

def search_sotu(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            print("IS VALID")
            term = form.cleaned_data['text_to_search']
            president = form.cleaned_data['president_to_search']
            date_start = form.cleaned_data['date_from']
            date_end = form.cleaned_data['date_through']
            if len(president) == 0:
                president = '%'
            else:
                president = '%' + president + '%'
            results = Speech.objects.raw(                    
                "SELECT id, president, title, speech_date, speech_text, " +
                "ts_headline(speech_text, websearch_to_tsquery('english', %s), " +
                "'StartSel = <b>, " +
                "StopSel = </b>, MinWords=5, MaxWords=80, MaxFragments=5, " +
                "FragmentDelimiter = \" ... <br/> ... \"') " +
                "FROM sotu_speech " +
                "WHERE search_speech_text @@ websearch_to_tsquery('english', %s) " +
                "AND president ILIKE %s " +
                "AND speech_date BETWEEN %s AND %s " +
                "ORDER BY speech_date DESC;",
                [term, term, president, date_start, date_end]
                )
            if len(results) == 0:
                results = 'None'
            return render(request,
                          'sotu_search.html',
                          {'form': form,
                           'term': term,
                           'results_list': results})
        else:
            print(form)
            print("NOT VALID")
    else:
        form = SearchForm()
    return render(request,
                  'sotu_search.html',
                  {'form': form})
