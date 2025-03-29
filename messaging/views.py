from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .models import Message
from .forms import MessageForm
from django.views.generic import ListView
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ConversationView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "messaging/conversation.html"
    context_object_name = "messages"
    ordering = ["-timestamp"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add list of users to enable starting new conversations
        context["users"] = User.objects.exclude(id=self.request.user.id)
        return context


class MessageListView(LoginRequiredMixin, ListView):  # Added LoginRequiredMixin
    model = Message
    template_name = "messaging/message_list.html"
    context_object_name = "messages"
    ordering = ["timestamp"]

    def get_queryset(self):
        other_user_id = self.kwargs.get("pk")
        current_user = self.request.user

        queryset = Message.objects.filter(
            models.Q(sender=current_user, receiver_id=other_user_id)
            | models.Q(receiver=current_user, sender_id=other_user_id)
        ).order_by("timestamp")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["other_user"] = User.objects.get(pk=self.kwargs.get("pk"))
        return context


class AddMessageView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = "messaging/add_message.html"

    def form_valid(self, form):
        form.instance.sender = self.request.user  # Automatically set sender
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the specific conversation
        return reverse("messaging:message_list", kwargs={"pk": self.object.receiver.pk})
