# Kit Team Committee Meeting 2023-02-13

- We had a discussion with a Trustee about an issue.
- We decided to start having a monthly committee meeting
- We discussed conflict resolution within the team.
- We discussed how to ensure quality of work going forward.
- We discussed contributor guidelines
- We are looking into a way to improve the above.

- Improving Kit Team Leadership
    - We will start having a monthly-ish committee-only meeting
    - Minutes will be published where appropriate, although possibly delayed if deemed necessary.
    - Some minutes may not be published for certain matters, e.g those concerning individual volunteers.
    - Normal Kit Team meetings will continue as usual, and are not replaced by committee meetings.

- Issues raised
    - A number of issues have been raised to the committee by a Trustee and multiple volunteers.
        - Some issues are interpersonal, some are technical and some are organisational
        - e.g Recent software releases have contained significant regressions during competition cycle.
    - We have decided that to address these issues, we need to introduce some extra guidance on how we work as a team.
    - Some changes will be introduced now, some will be delayed until after the competition
    - The committee will review progress on raised issues regularly.
    - Feedback is welcomed from all members of the organisation, any change is not set in concrete.

- Introduce Repository Maintainers
    - We can work with the infrastructure team to use `CODEOWNERS`
    - We will put together a list of repositories and who maintains them.
    - Ideally 2 maintainers per repository
    - Maintainer Responsibilities
        - "Owns" the code
        - Security fixes
        - reviewing PRs
        - are not expected to write everything
        - Act in the best interests of Student Robotics
        - Marks releases and tags
            - Only maintainers have permissions to mark releases or tags.
            - Protected Tags
    - Assignment of Maintainers
        - We need to work how to assign
    - Removal of Maintainer
        - i.e if a maintainer does not want to be a maintainer anymore
        - This would only happen with good reason, and with consent.
        - need to make sure volunteer workload is manageable.
        - No in-use projects should be left maintained
    - **We aim to introduce this after the SR2023 competition**

- Software Supply Chain
    - All non-standard library software must be in the `srobo` GitHub
        - Software Supply Chain attacks
        - If external, it will be a fork.
            - This will be determined by whether the software would be suitable for inclusion in Debian.
            - e.g `libc` is standard, `zoloto` is not.
            - The fork maintainer must not be the same as the upstream maintainer.
                - e.g if `sam_smith` maintains `ssmith/libfoo`, then the maintainer of `srobo/libfoo` cannot be `sam_smith`
            - When the internal maintainer rebases the fork, they must review the changes.
        - All images must be built from our copies, or sources that we control.
        - This ensures that all custom software follows our maintainer process.
        - This also ensures that we are compliant with Open Source software licences.
    - **We aim to be compliant with this for SR2024 software builds**

- Software QA 
    - All shipped images must be built from a tagged release on the `main` branch
    - If necessary, we could introduce a stable branch.
    - All dependencies in a release must be a tagged version and approved by the relevant maintainer.
    - We urgently need a proper review process
        - The image must be tested by somebody other than the person that built the image, on a physical kit.
        - The release of an image to students must be approved by a kit team committee member.
            - i.e the PR to updates `docs` with the new version must be approved.
            - We should consider adding CODEOWNERS to the docs repo to enforce this.
    - Software Release Owner
        - Somebody owns the release.
        - Responsible for getting it ready, tested and approved
        - Not necessarily the person writing the code, but the one chasing things
        - Checking all dependencies are tagged versions
        - Updating the docs with contained versions (i.e Python libs)
        - The owner holds us to account to make sure we meet image deadlines without compromising quality.
        - This would usually be assigned in a kit team meeting (or by the committee)
            - Although in the case of urgent releases, assignment may be more ad-hoc.
    - This prevents images being released without thorough testing, whilst still allowing volunteers to release an urgent update in a short timespan.
    - **We aim for this to be enforced from the Kit Team meeting on 7th March**

- Contributor Guidelines
    - How to respond, both for reviewer and contributor
    - Treat each other excellently.
    - Explain decisions with context and reason.
        - Consider messaging them or talking in a call.
        - Allow response from the other person
        - Don't act with haste.
        - Remember there are other things in people's lives.
    - **We plan to work with other SR teams to introduce this by SR2024**

- Code Standards
    - We should consider introducing a standard set of code guidelines
    - Enforced across all repos
    - Maybe not blocking on some repos.
    - Something to think about how we do.
        - Maybe with the infrastructure
    - Shared GitHub Action?
        - `srobo/lint`?
    - Common tooling lowers the barrier for new and existing volunteering to get involved.
    - **We plan to work with other SR teams to introduce this by SR2024**

- Kit Design Reviews
    - We discussed ideas for a process for discussing significant changes to the kit.
    - We have decided not to go ahead with this

- Roadmap process
    - We should formalise this, but not a priority as we have a roadmap for SR2024

**The Kit Team Committee welcome all and any feedback on suggested changes.**
