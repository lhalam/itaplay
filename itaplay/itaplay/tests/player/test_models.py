from django.test import TestCase
from player.models import Player
from company.models import Company
from projects.models import AdviserProject


class PlayerTestCase(TestCase):

    def setUp(self):
        _company = Company(
            company_zipcode="79008",
            company_logo="http://test.test",
            company_name="testcompany",
            company_mail="test@test.test",
            company_phone="+380901234567",
        )
        _company.save()
        _project = AdviserProject(
            id_company=_company,
            name="project1",
            description="test",
            project_template="test",
        )
        _project.save()

        self.first = [Player.objects.create(
                    id=1,
                    name="player1",
                    description="player description",
                    mac_address="11:2a:bb:q1:ss:77",
                    status=False,
                    project=_project),
                 Player.objects.create(
                    id=2,
                    name="player2",
                    description="player2 description",
                    mac_address="88:2a:bb:q1:ss:88",
                    status=False,
                    project=_project)
                ]

    def test_player_get_by_Player(self):
        player = Player.objects.get(id=1)
        self.assertEqual(player.name, "player1")
        self.assertEqual(player.mac_address, "11:2a:bb:q1:ss:77")
        self.assertEqual(player.description, "player description")
        self.assertFalse(player.status)

    def test_player_set(self):
        test = Player(id=10,
                      name="player3",
                      description="player3 description",
                      mac_address="00:00:00:q1:ss:88",
                      status=False)
        test.save()
        self.assertEqual(test.name, "player3")
        self.assertEqual(test.mac_address, "00:00:00:q1:ss:88")

    def test_player_delete_by_id(self):
        Player.delete_by_id(1)
        try:
            Player.objects.get(1)
        except TypeError:
            pass

    def test_player_get_all(self):
        test = Player.get_all()
        self.assertEqual(len(test), len(self.first))

    def test_player_get_by_id(self):
        test = Player.get_by_id(1)
        self.assertEqual(test.name, 'player1')

    def test_player_get_None(self):
        test = Player.get_by_id(33)
        self.assertIsNone(test)



