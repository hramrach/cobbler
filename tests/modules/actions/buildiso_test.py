import pytest

from cobbler.actions.buildiso import BuildIso


class TestBuildiso:
    @pytest.mark.parametrize("input_kopts_dict,exepcted_output", [
        ({}, "")
    ])
    def test_add_remaining_kopts(self, input_kopts_dict, exepcted_output):
        # Arrange (missing)
        # Act
        output = BuildIso.add_remaining_kopts(input_kopts_dict)

        # Assert
        assert output == exepcted_output

    def test_make_shorter(self):
        # Arrange
        buildiso = BuildIso()

        # Act
        buildiso.make_shorter()

        # Assert
        assert False

    def test_copy_boot_files(self):
        # Arrange
        buildiso = BuildIso()

        # Act
        buildiso.copy_boot_files()

        # Assert
        assert False

    def test_filter_systems_or_profiles(self):
        # Arrange
        buildiso = BuildIso()

        # Act
        buildiso.filter_systems_or_profiles()

        # Assert
        assert False

    def test_generate_netboot_iso(self):
        # Arrange
        buildiso = BuildIso()

        # Act
        buildiso.generate_netboot_iso()

        # Assert
        assert False

    def test_generate_standalone_iso(self):
        # Arrange
        buildiso = BuildIso()

        # Act
        buildiso.generate_standalone_iso()

        # Assert
        assert False

    def test_run(self):
        # Arrange
        buildiso = BuildIso()

        # Act
        buildiso.run()

        # Assert
        assert False