from django.shortcuts import render, redirect, reverse
from .models import Lead
from .forms import LeadForm
from django.views import generic


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

def landing_page(request):
    return render(request, "landing.html")

class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = 'leads'

def lead_list(request):
    leads = Lead.objects.all()
    context = {'leads':leads}
    return render(request, "leads/lead_list.html", context)

class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = 'lead'

def lead_detail(request,pk):
    lead = Lead.objects.get(id=pk)
    print(pk)
    
    context = {'lead':lead}
    return render(request, 'leads/lead_detail.html', context)

class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadForm
    
    def get_success_url(self):
        return reverse('lead_list')
    
def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {'form':form}
    return render(request, 'leads/lead_create.html', context)


class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadForm
    
    def get_success_url(self):
        return reverse('lead_list')
def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadForm(instance=lead)
    if request.method == "POST":
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {'lead':lead, 'form':form}
    return render(request, 'leads/lead_update.html', context)

class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()