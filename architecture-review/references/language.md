# Architecture Language

Use the same terms in every architecture suggestion.

## Terms

**Module**
Anything with an interface and an implementation: function, class, package, workflow slice, or subsystem.

**Interface**
Everything a caller must know to use a module correctly. This includes signatures, invariants, ordering, errors, config, and performance expectations.

**Implementation**
The code hidden behind the interface.

**Seam**
A place where behavior can change without editing callers. Avoid "boundary" unless discussing DDD bounded contexts.

**Adapter**
A concrete implementation behind a seam.

**Depth**
Leverage at the interface: a large amount of behavior behind a small, stable contract.

**Locality**
The degree to which change, bugs, knowledge, and verification are concentrated in one place.

## Principles

- Depth is a property of the interface, not line count.
- The interface is the test surface.
- One adapter means a hypothetical seam. Two adapters means a real seam.
- The deletion test: if deleting a module removes complexity, it was likely shallow; if complexity reappears across callers, it was earning its keep.
- Prefer domain-shaped seams over technology-shaped seams when domain concepts drive the behavior.
