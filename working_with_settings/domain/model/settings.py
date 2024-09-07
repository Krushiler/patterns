class Settings:
    def __init__(self):
        self._organization_name = ''
        self._inn = ''
        self._director_name = ''

    @property
    def organization_name(self):
        return self._organization_name

    @organization_name.setter
    def organization_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError('organization_name must be str')
        self._organization_name = value

    @property
    def inn(self):
        return self._inn

    @inn.setter
    def inn(self, value: str):
        if not isinstance(value, str):
            raise TypeError('inn must be str')
        if not value.isdigit():
            raise ValueError('inn must be digits')
        if len(value) != 12:
            raise ValueError('inn must be 12 chars long')
        self._inn = value

    @property
    def director_name(self):
        return self._director_name

    @director_name.setter
    def director_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError('director_name must be str')
        self._director_name = value

    def __str__(self):
        return f'organization_name: {self.organization_name}, inn: {self.inn}, director_name: {self.director_name}'
