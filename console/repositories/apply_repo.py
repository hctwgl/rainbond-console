# -*- coding: utf-8 -*-
from console.models import Applicants


class ApplyRepo(object):

    def get_applicants(self, team_name):
        return Applicants.objects.filter(team_name=team_name)

    def get_applicants_team(self, user_id):
        return Applicants.objects.filter(user_id=user_id)

    def get_applicants_by_id_team_name(self, user_id, team_name):
        return Applicants.objects.filter(user_id=user_id, team_name=team_name)

    def create_apply_info(self, **params):
        return Applicants.objects.create(**params)


apply_repo = ApplyRepo()
