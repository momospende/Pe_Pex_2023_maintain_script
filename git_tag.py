import argparse
import git


def set_git_tag(tag, commit):
    repo = git.Repo()
    try:
        repo.git.tag(tag, commit, m=tag)
        repo.remotes.origin.push(tag)
    except git.GitCommandError as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set a git tag on a commit.")
    parser.add_argument("tag", help="Name of the tag")
    parser.add_argument("commit", help="Commit to tag")
    args = parser.parse_args()

    set_git_tag(args.tag, args.commit)
