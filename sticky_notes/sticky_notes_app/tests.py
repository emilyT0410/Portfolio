from django.test import TestCase
from django.contrib.auth.models import User as djUser
from django.test.client import Client
from sticky_notes_app.models import User, StickyNote
from django.urls import reverse


# Create your tests here.
class UserModelTest(TestCase):
    """Testing the User Model"""

    def setUp(self) -> None:
        """Set up a test user with 'test' for username, password and email"""
        user = User.objects.create(username="test", password="test", email="test")

    def test_user_username(self):
        """Test the user has the expected username"""
        user = User.objects.get(id=1)
        self.assertEqual(user.username, "test")

    def test_user_password(self):
        """Test the user has the expected password"""
        user = User.objects.get(id=1)
        self.assertEqual(user.password, "test")

    def test_user_email(self):
        """Test the user has the expected email"""
        user = User.objects.get(id=1)
        self.assertEqual(user.email, "test")


class StickyNoteModelTest(TestCase):
    """Testing the Sticky Note Model"""

    def setUp(self) -> None:
        """Set up a test note with title, description"""
        sticky_note = StickyNote.objects.create(
            title="Test title", description="This is a test description"
        )

    def test_stickynote_title(self):
        """Test the note has the expected title"""
        sticky_note = StickyNote.objects.get(id=1)
        self.assertEqual(sticky_note.title, "Test title")

    def test_stickynote_description(self):
        """Test the note has the expected description"""
        sticky_note = StickyNote.objects.get(id=1)
        self.assertEqual(sticky_note.description, "This is a test description")


class IndexViewTest(TestCase):
    """Testing the function that lists all the sticky notes. NB: Uses @LoginRequired decorator"""

    def setUp(self) -> None:
        """Set up a test note with title, description"""
        sticky_note = StickyNote.objects.create(
            title="Test title", description="This is a test description"
        )
        # Function uses @Loginrequired decorator so we need to log in to test this
        self.client = Client()
        self.user = djUser.objects.create_user("test", "test", "test")

    def test_index_with_input(self):
        """Test the index function"""
        self.client.login(username="test", password="test")  # Log in
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test title")


class AddNoteViewTest(TestCase):
    """Testing the function that allows the user to create a new note. NB: Uses @LoginRequired decorator"""

    def setUp(self) -> None:
        """Set up a test note with title, description"""
        sticky_note = StickyNote.objects.create(
            title="Test title", description="This is a test description"
        )
        # Function uses @Loginrequired decorator so we need to log in to test this
        self.client = Client()
        self.user = djUser.objects.create_user("test", "test", "test")

    def test_add_note_with_input(self):
        """Test the create new sticky note function"""
        self.client.login(username="test", password="test")  # Log in
        add_sticky_note = StickyNote.objects.create(
            title="New", description="This is a new description"
        )
        response = self.client.get(reverse("add_note"))
        self.assertContains(response, "New")


class ViewNoteViewTest(TestCase):
    """Testing the function that views a specific sticky note. NB: Uses @LoginRequired decorator"""

    def setUp(self) -> None:
        """Set up a test note with title, description"""
        sticky_note = StickyNote.objects.create(
            title="Test title", description="This is a test description"
        )
        # Function uses @Loginrequired decorator so we need to log in to test this
        self.client = Client()
        self.user = djUser.objects.create_user("test", "test", "test")

    def test_view_note_with_input(self):
        """Test the view note function with given input.
        This should allow the user to view the note: title,
        description and time created"""
        self.client.login(username="test", password="test")  # Log in
        sticky_note = StickyNote.objects.get(id=1)
        response = self.client.get(reverse("view_note", args=[str(sticky_note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test title")
        self.assertContains(response, "This is a test description")


class EditNoteViewTest(TestCase):
    """Test the function that allows the user to edit the sticky note title
    and/or description. NB: Uses @LoginRequired decorator"""

    def setUp(self) -> None:
        """Set up a test note with title, description"""
        sticky_note = StickyNote.objects.create(
            title="Test title", description="This is a test description"
        )
        # Function uses @Loginrequired decorator so we need to log in to test this
        self.client = Client()
        self.user = djUser.objects.create_user("test", "test", "test")

    def test_edit_note(self):
        """test the edit note function with given changes"""
        self.client.login(username="test", password="test")  # Log in
        sticky_note = StickyNote.objects.get(id=1)
        updated_note = StickyNote.objects.update(title="Updated title")
        response = self.client.get(reverse("edit_note", args=[str(sticky_note.id)]))
        self.assertContains(response, "Updated title")


class DeleteNoteViewTest(TestCase):
    """Test the function that allows the user to delete a specific note NB: Uses @LoginRequired decorator"""

    def setUp(self) -> None:
        """Set up a test note with title, description"""
        sticky_note = StickyNote.objects.create(
            title="Test title", description="This is a test description"
        )
        # Function uses @Loginrequired decorator so we need to log in to test this
        self.client = Client()
        self.user = djUser.objects.create_user("test", "test", "test")

    def test_delete_note(self):
        """test the delete note function removing the test note"""
        self.client.login(username="test", password="test")  # Log in
        sticky_note = StickyNote.objects.get(id=1)
        sticky_note.delete()
        # Check it has been removed from the main list of notes
        response = self.client.get(reverse("index")) 
        self.assertNotContains(response, "Test title")
