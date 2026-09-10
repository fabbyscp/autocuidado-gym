import pytest
import banco


@pytest.fixture(autouse=True)
def banco_de_teste(tmp_path, monkeypatch):
    banco_teste = tmp_path / "teste.db"

    monkeypatch.setattr(banco, "DATABASE", str(banco_teste))

    banco.criar_tabela()