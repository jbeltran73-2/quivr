from uuid import UUID

from models.databases.supabase.onboarding import OnboardingUpdatableProperties
from models.onboarding import Onboardings
from models.settings import get_supabase_db


def update_user_onboarding(
    user_id: UUID, onboarding: OnboardingUpdatableProperties
) -> Onboardings:
    """Update user onboarding information by user_id"""

    supabase_db = get_supabase_db()
    return supabase_db.update_user_onboarding(user_id, onboarding)
