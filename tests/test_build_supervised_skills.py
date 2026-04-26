import importlib.util
from pathlib import Path


def load_builder(repo_root: Path):
    module_path = repo_root / "scripts" / "build_supervised_skills.py"
    spec = importlib.util.spec_from_file_location("build_supervised_skills", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def write_skill(root: Path, name: str, body: str = "Skill body.\n") -> None:
    skill_dir = root / name
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: Use when testing {name}.\n---\n\n# {name}\n\n{body}",
        encoding="utf-8",
    )
    (skill_dir / "notes.txt").write_text("copy me\n", encoding="utf-8")


def test_build_supervised_copies_clean_skill_and_appends_footer(tmp_path: Path) -> None:
    repo = tmp_path
    write_skill(repo, "example-skill")
    (repo / "skill-supervisor").mkdir()
    (repo / "skill-supervisor" / "SKILL.md").write_text(
        "---\nname: skill-supervisor\ndescription: Use when evaluating skills.\n---\n",
        encoding="utf-8",
    )
    (repo / "vendor").mkdir()

    builder = load_builder(Path.cwd())
    built = builder.build_supervised_skills(repo)

    assert built == ["example-skill"]
    supervised_skill = repo / "supervised" / "example-skill" / "SKILL.md"
    assert supervised_skill.exists()
    text = supervised_skill.read_text(encoding="utf-8")
    assert "# example-skill" in text
    assert "Skill Supervisor Footer" in text
    assert '"skill": "example-skill"' in text
    assert (repo / "supervised" / "example-skill" / "notes.txt").read_text(
        encoding="utf-8"
    ) == "copy me\n"
    assert not (repo / "supervised" / "skill-supervisor").exists()


def test_build_supervised_replaces_stale_generated_output(tmp_path: Path) -> None:
    repo = tmp_path
    write_skill(repo, "example-skill")
    stale = repo / "supervised" / "old-skill"
    stale.mkdir(parents=True)
    (stale / "SKILL.md").write_text("stale\n", encoding="utf-8")

    builder = load_builder(Path.cwd())
    builder.build_supervised_skills(repo)

    assert not stale.exists()
    assert (repo / "supervised" / "example-skill" / "SKILL.md").exists()
