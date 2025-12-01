fastapi-k8s-app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── dependencies.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── router.py
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           ├── health.py
│   │           ├── items.py
│   │           └── users.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── logging.py
│   │   ├── security.py
│   │   └── middleware.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── session.py
│   │   ├── base.py
│   │   └── models/
│   │       ├── __init__.py
│   │       └── item.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── item.py
│   └── services/
│       ├── __init__.py
│       └── item_service.py
├── k8s/
│   ├── base/
│   │   ├── namespace.yaml
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   ├── configmap.yaml
│   │   ├── secret.yaml
│   │   └── hpa.yaml
│   ├── overlays/
│   │   ├── dev/
│   │   │   ├── kustomization.yaml
│   │   │   └── patches/
│   │   ├── staging/
│   │   │   ├── kustomization.yaml
│   │   │   └── patches/
│   │   └── prod/
│   │       ├── kustomization.yaml
│   │       └── patches/
│   └── ingress/
│       └── ingress.yaml
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   │   └── test_items.py
│   └── integration/
│       └── test_api.py
├── scripts/
│   ├── entrypoint.sh
│   ├── healthcheck.sh
│   └── migrate.sh
├── .github/
│   └── workflows/
│       ├── ci.yaml
│       └── cd.yaml
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
├── .env.example
├── alembic.ini
├── README.md
└── Makefile