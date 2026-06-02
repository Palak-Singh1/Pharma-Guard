from pydantic import BaseModel, Field
from typing import List, Literal
from datetime import datetime


# ---------------------------
# Nested Models
# ---------------------------

class RiskAssessment(BaseModel):
    risk_label: Literal["Safe", "Adjust Dosage", "Toxic", "Ineffective", "Unknown"]
    confidence_score: float
    severity: Literal["none", "low", "moderate", "high", "critical"]

    class Config:
        extra = "forbid"


class DetectedVariant(BaseModel):
    rsid: str

    class Config:
        extra = "forbid"


class PharmacogenomicProfile(BaseModel):
    primary_gene: str
    diplotype: str
    phenotype: Literal["PM", "IM", "NM", "RM", "URM", "Unknown"]
    detected_variants: List[DetectedVariant]

    class Config:
        extra = "forbid"


class ClinicalRecommendation(BaseModel):
    recommendation: str

    class Config:
        extra = "forbid"


class LLMGeneratedExplanation(BaseModel):
    summary: str

    class Config:
        extra = "forbid"


class QualityMetrics(BaseModel):
    vcf_parsing_success: bool

    class Config:
        extra = "forbid"


# ---------------------------
# Main Response Model
# ---------------------------

class PharmacogenomicResponse(BaseModel):
    patient_id: str
    drug: str
    timestamp: datetime
    risk_assessment: RiskAssessment
    pharmacogenomic_profile: PharmacogenomicProfile
    clinical_recommendation: ClinicalRecommendation
    llm_generated_explanation: LLMGeneratedExplanation
    quality_metrics: QualityMetrics

    class Config:
        extra = "forbid"
